"""
Gregory Way 2018
bsub-help.py

Usage: Import only

    from bsub-help import bsubHelp

    b = bsubHelp(command=command, queue=queue)

    b.make_command_list()    # To make a python list of commands
    b.make_command_string()  # To make a python string of commands
    b.submit_command()       # Directly submit bsub job to cluster
"""

import subprocess


class bsubHelp():
    def __init__(self, command, queue, job_name='default', num_cpus=1,
                 num_gpus=1, num_ram=8, num_gpus_shared=0, walltime='0:10',
                 error_file='std_err.txt', output_file='std_out.txt',
                 depend_job='None', local=False, shell=True):
        try:
            self.command = command.split(' ')
        except:
            self.command = command
        self.queue = queue
        self.job_name = job_name
        self.num_cpus = num_cpus
        self.num_gpus = num_gpus
        self.num_ram = num_ram
        self.num_gpus_shared = num_gpus_shared
        self.walltime = walltime
        self.error_file = error_file
        self.output_file = output_file
        self.depend_job = depend_job
        self.local = local
        self.shell = shell

    def make_command_list(self):
        command_list = ['bsub', '-q', self.queue, '-J', self.job_name,
                        '-eo', self.error_file, '-oo', self.output_file,
                        '-c', self.walltime]
        if self.queue == 'gpu':
            command_list += ['-R',
                             '"select[ngpus>{}] rusage [ngpus_shared={}]"'
                             .format(self.num_gpus, self.num_gpus_shared)]
        else:
            command_list += ['-n', self.num_cpus, '-R',
                             '"rusage[mem={}]"'.format(self.num_ram)]
        if self.depend_job != 'None':
            command_list += ['-w', '"done({})"'.format(self.depend_job)]
        command_list += self.command
        return command_list

    def make_command_string(self):
        if self.local:
            return self.command
        else:
            command_string = (
                'bsub -q {} -J {}, -eo {} -oo {} -c {}'
                .format(self.queue, self.job_name, self.error_file,
                        self.output_file, self.walltime)
                )
            if self.queue == 'gpu':
                command_string = (
                    '{} -R "select[ngpus>{}] rusage [ngpus_shared={}]"'
                    .format(command_string, self.num_gpus,
                            self.num_gpus_shared)
                    )
            else:
                command_string = (
                    '{} -n {} -R "rusage[mem={}]"'
                    .format(command_string, self.num_cpus, self.num_ram)
                )
            if self.depend_job != 'None':
                command_string = (
                    '{} -w "done({})"'.format(command_string, self.depend_job)
                )
            return '{} {}'.format(command_string, ' '.join(self.command))

    def submit_command(self):
        if self.local:
            submit_command = self.make_command_list()
        else:
            submit_command = self.make_command_string()
        subprocess.call(submit_command, shell=self.shell)
