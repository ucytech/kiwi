from nose.tools import *
from mock import patch

import mock

import nose_helper

from kiwi.bootloader_template_isolinux import BootLoaderTemplateIsoLinux


class TestBootLoaderTemplateIsoLinux(object):
    def setup(self):
        self.isolinux = BootLoaderTemplateIsoLinux()

    def test_get_multiboot_install_template(self):
        assert self.isolinux.get_multiboot_install_template().substitute(
            default_boot='0',
            kernel_file='linux.vmx',
            initrd_file='initrd.vmx',
            boot_options='splash',
            failsafe_boot_options='splash',
            gfxmode='800x600',
            theme='SLE',
            boot_timeout='10',
            title='LimeJeOS-SLE12-Community [ VMX ]',
            bootpath='/boot',
            hypervisor='xen.gz'
        )

    def test_get_install_template(self):
        assert self.isolinux.get_install_template().substitute(
            default_boot='0',
            kernel_file='boot/linux.vmx',
            initrd_file='boot/initrd.vmx',
            boot_options='cdinst=1 splash',
            failsafe_boot_options='cdinst=1 splash',
            gfxmode='800x600',
            theme='SLE',
            boot_timeout='10',
            title='LimeJeOS-SLE12-Community [ VMX ]',
            bootpath='/boot'
        )

    def test_get_multiboot_install_template_plain_ui(self):
        assert self.isolinux.get_multiboot_install_template(
            with_theme=False
        ).substitute(
            default_boot='0',
            kernel_file='linux.vmx',
            initrd_file='initrd.vmx',
            boot_options='splash',
            failsafe_boot_options='splash',
            gfxmode='800x600',
            theme='SLE',
            boot_timeout='10',
            title='LimeJeOS-SLE12-Community [ VMX ]',
            bootpath='/boot',
            hypervisor='xen.gz'
        )

    def test_get_install_template_plan_ui(self):
        assert self.isolinux.get_install_template(with_theme=False).substitute(
            default_boot='0',
            kernel_file='boot/linux.vmx',
            initrd_file='boot/initrd.vmx',
            boot_options='cdinst=1 splash',
            failsafe_boot_options='cdinst=1 splash',
            gfxmode='800x600',
            theme='SLE',
            boot_timeout='10',
            title='LimeJeOS-SLE12-Community [ VMX ]',
            bootpath='/boot'
        )

    def test_get_message_template(self):
        assert self.isolinux.get_message_template().substitute(
            title='LimeJeOS-SLE12-Community [ VMX ]'
        )

    def test_get_install_message_template(self):
        assert self.isolinux.get_install_message_template().substitute(
            title='LimeJeOS-SLE12-Community [ VMX ]'
        )