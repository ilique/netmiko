from netmiko.cisco_base_connection import BaseConnection
import re
import time


class DlinkBase(BaseConnection):
    def save_config(self, cmd="", confirm=True, confirm_response=""):
        # TODO: do we need this?
        pass

    def exit_enable_mode(self, **kwargs):
        pass

    def config_mode(self, **kwargs):
        return ''

    def exit_config_mode(self, **kwargs):
        pass

    def session_preparation(self):
        pass

    # def set_base_prompt(self, pri_prompt_terminator='#',
    #                     alt_prompt_terminator='#', delay_factor=1):
    #     fPrompt = self.find_prompt(delay_factor=delay_factor)
    #     prompt = fPrompt.split(':')
    #     if not prompt[-1] in ('user#', 'admin#', '3#', '4#', '5#'):
    #         raise ValueError("Router prompt not found: {0}".format(repr(prompt)))
    #     # Strip off trailing terminator
    #     self.base_prompt = prompt[0]
    #
    #     return self.base_prompt

    def check_enable_mode(self, check_string=''):
        self.write_channel(self.RETURN)
        output = self.read_until_prompt()
        pattern = re.compile("(admin#|4#|5#)")

        return pattern.search(output) is not None

    def enable(self, cmd='enable admin', **kwargs):
        self.base_prompt = "#"
        return super().enable(cmd=cmd)

    def disable_paging(self, command="disable clipaging", delay_factor=1):
        return super(DlinkBase, self).disable_paging(command=command)


class DlinkSSH(DlinkBase):
    pass


class DlinkTelnet(DlinkBase):
    pass