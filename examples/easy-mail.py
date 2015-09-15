#!/usr/bin/python
"""
Easy way of sending HTML mails using templates.

=======
License
=======
Copyright (c) 2015 Thomas Lehmann

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons
to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies
or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import sys
import platform
import os
import click
import yaml
import smtplib

from concept import VERSION
from shutil import copyfile
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from jinja2 import Environment, FileSystemLoader

DEFAULT_TEMPLATE_PATH = os.path.dirname(os.path.abspath(__file__))
DEFAULT_TEMPLATE = "easy-mail.html"
DEFAULT_CONFIGURATION = os.path.join(os.path.dirname(os.path.abspath(__file__)), "easy-mail.yml")
HOME_CONFIGURATION = os.path.join(os.environ["HOME"], "easy-mail.yml")
TMP_FILE = "/tmp/easy-html-content.html"


def get_configuration_file():
    """ ensure yml file exist at $HOME and providing file path and name. """
    if not os.path.isfile(HOME_CONFIGURATION):
        copyfile(DEFAULT_CONFIGURATION, HOME_CONFIGURATION)
    return HOME_CONFIGURATION


def send_mail(configuration, content):
    """ sending a HTML mail. """
    server = configuration['communication']['server']
    port = int(configuration['communication']['port'])
    sender = configuration['communication']['sender']
    password = str(configuration['communication']['password'])
    # "yes" will be mapped to a boolean value
    tls = configuration['communication']['tls']
    ssl = configuration['communication']['ssl']

    message = MIMEMultipart()
    message['Subject'] = configuration['subject']
    message['From'] = sender
    message['To'] = ",".join(configuration['recipients'])

    for entry in configuration['attachment']:
        if os.path.isfile(entry):
            print(" ... attaching file %s" % entry)
            attachment = MIMEApplication(
                open(entry, "rb").read(),
                Content_Disposition="attachment; filename=%s" % os.path.basename(entry),
                Name=os.path.basename(entry))
            message.attach(attachment)
        else:
            print(" ... file not found: %s" % entry)
            print(" ... do not send mail")
            return

    image_number = 1
    for entry in configuration['images']:
        if os.path.isfile(entry):
            print(" ... embedding image %s" % entry)
            image = MIMEImage(open(entry, "rb").read())
            image.add_header('Content-ID', "<image%d>" % image_number)
            image_number += 1
            message.attach(image)
        else:
            print(" ... image not found: %s" % entry)
            print(" ... do not send mail")
            return

    body = MIMEText(content, 'html')
    message.attach(body)

    if ssl:
        print(" ... creating SSL session")
        session = smtplib.SMTP_SSL(server, port)
    else:
        print(" ... creating none SSL session")
        session = smtplib.SMTP(server, port)

    if tls:
        print(" ... starting tls session")
        session.starttls()
    if len(password) > 0 and not password.lower() == "none":
        print(" ... login")
        session.login(sender, password)
    print(" ... send message")
    session.sendmail(sender, configuration['recipients'], message.as_string())
    session.quit()


@click.command()
@click.option("--configuration", default=get_configuration_file(),
              help="path and filename of configuration")
@click.option("--template-path", default=DEFAULT_TEMPLATE_PATH,
              help="path for templates")
@click.option("--template", default=DEFAULT_TEMPLATE,
              help="filename of template")
@click.option("--check", default=False,
              help="view HTML in browser to check content")
def main(configuration, template_path, template, check):
    """ Easy way of sending a HTML mail. """
    print("easy-mail tool (version %s)" % VERSION)
    print(" ... Python %s" % sys.version.replace("\n", ""))
    print(" ... Platform %s" % platform.platform())
    print(" ... Used configuration %s" % configuration)
    print(" ... Used template %s" % (os.path.join(template_path, template)))

    # reading yaml file into a dictionary
    configuration_content = yaml.load(open(configuration).read())
    # rendering HTML content (hope it is HTML)
    environment = Environment(loader=FileSystemLoader(template_path))
    template_renderer = environment.get_template(template)
    final_content = template_renderer.render(configuration=configuration_content)
    if check:
        import webbrowser
        handle = open(TMP_FILE, "w")
        handle.write(final_content)
        handle.close()
        webbrowser.open_new_tab("file://%s" % TMP_FILE)
    else:
        send_mail(configuration_content, final_content)

if __name__ == "__main__":
    main()
