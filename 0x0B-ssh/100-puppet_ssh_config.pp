# set up your client SSH configuration file so that you can connect to a
# server without typing a password.

exec { 'config SSH client':
  command => "echo -e 'IdentityFile ~/.ssh/school\nPasswordAuthentication no\n' >> /etc/ssh/ssh_config",
  path    => '/bin:/usr/bin',
}
