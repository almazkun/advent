inpt = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

    def __repr__(self):
        if self.parent:
            return str(f"{self.parent}/{self.name}")
        return str("dir:/")


class File:
    def __init__(self, name: str, dir: Dir, size: int):
        self.name = name
        self.dir = dir
        self.size = size


def parse_cmd(line, cwd, dirs, files):
    _, cmd, *arg = line.split(" ")
    arg = arg[0] if arg else arg
    if cmd == "cd":
        if arg == "..":
            cwd = cwd.parent
        elif any([dir.name == arg for dir in dirs]):
            dir = [dir for dir in dirs if dir.name == arg].pop()
            cwd = dir
        else:
            dir = Dir(name=arg, parent=cwd)
            dirs.append(dir)
            cwd = dir
    elif cmd == "ls":
        pass
    print(cwd, dirs, files)
    return cwd, dirs, files


def parse_line(line, cwd, dirs, files):
    if line.startswith("$"):
        return parse_cmd(line, cwd, dirs, files)
    return cwd, dirs, files


def main():
    dirs = []
    files = []

    cwd = Dir(name="/", parent=None)
    dirs.append(cwd)

    for line in inpt.split("\n"):
        cwd, dirs, files = parse_line(
            line,
            cwd,
            dirs,
            files,
        )

    print(cwd, dirs, files)


if __name__ == "__main__":
    main()
