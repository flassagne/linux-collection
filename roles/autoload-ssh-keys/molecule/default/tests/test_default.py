"""Role testing files using testinfra."""


def test_check_prereq(host):
    assert host.package("ksshaskpass").is_installed


def test_ssh_ask_pass(host):
    ssh_ask_pass = host.file("/root/.config/autostart-scripts/ask_pass.sh")

    assert ssh_ask_pass.exists
    assert ssh_ask_pass.mode == 0o744
    assert ssh_ask_pass.contains("/usr/bin/ksshaskpass")


def test_ssh_add(host):
    ssh_add = host.file("/root/.config/autostart-scripts/ssh_add.sh")

    assert ssh_add.exists
    assert ssh_add.mode == 0o744
    assert ssh_add.contains("ssh-add -q ~/.ssh/id_rsa_stub")
