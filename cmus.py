from ranger.api.commands import *

def get_files(fm):
    ftd = fm.thisdir
    selected_files = ftd.get_selection()
    active_file = fm.thisfile if not selected_files else None

    if not selected_files and not active_file:
        return
    else:
        file_objs = selected_files if selected_files else [active_file]
    return file_objs

class cmus_playlist(Command):
    def execute(self):
        """ Add selected files or folders to playlist """
        file_objs = get_files(self.fm)

        cmus = ["cmus-remote"]
        cmus.extend([f.path for f in file_objs])
        self.fm.execute_command(cmus)
        self.fm.notify("Files were sent to cmus playlist")
        self.fm.thisdir.mark_all(False)

class cmus_queue(Command):
    def execute(self):
        """ Add selected files or folders to queue """

        file_objs = get_files(self.fm)
        cmus = ["cmus-remote", "-q"]
        cmus.extend([f.path for f in file_objs])
        self.fm.execute_command(cmus)
        self.fm.notify("Files were sent to cmus queue")
        self.fm.thisdir.mark_all(False)

class cmus_lib(Command):
    def execute(self):
        """ Add selected files or folders to library """

        file_objs = get_files(self.fm)
        cmus = ["cmus-remote", "-l"]
        cmus.extend([f.path for f in file_objs])
        self.fm.execute_command(cmus)
        self.fm.notify("Files were sent to cmus library")
        self.fm.thisdir.mark_all(False)

class cmus_play(Command):
    def execute(self):
        """ Play selected files or folders """
        file_objs = get_files(self.fm)

        cmus1 = ["cmus-remote", "-c", "-q"]
        self.fm.execute_command(cmus1)
        cmus2 = ["cmus-remote", "-q"]
        cmus2.extend([f.path for f in file_objs])
        self.fm.execute_command(cmus2)
        cmus3 = ["cmus-remote", "-n", "-p"]
        self.fm.execute_command(cmus3)
        self.fm.notify("Cmus queue was cleared and files were sent to it.")
        self.fm.thisdir.mark_all(False)


class cmus_pause(Command):
    def execute(self):
        """ Toggle pause playing music """

        cmus = ["cmus-remote", "-u"]
        self.fm.execute_command(cmus)
        self.fm.thisdir.mark_all(False)
