# Salesforce Tools

A project with some basic tools for working with Salesforce.

## Configuration

These scripts expect credentials in ``$XDG_CONFIG_HOME/salesforce/credentials`` or ``$HOME/.config/salesforce/credentials``.
The credentials are currently stored as JSON, as follows::

  {
    "password": "my_password",
    "username": "my_login@example.com",
    "security_token": "my_security_token"
  }
