#pre-commit hook

##Installation
1. make sure python 2 get installed and be available at environment path
1. install xsrc
2. run xsrc to init your reposet
3. run `xsrc install -hook pre-commit -r some-repo`
4. done

##Usage
1. This hook tests if source files are licensed under Apache or GPL, if not, will warn users and stop committing until fix it. Currently following types of source are checked out,

    '.m', '.mm', '.h', '.cpp', '.c', '.cs', '.java', '.js', '.html'
2. Because the hook cannot detect everything, when there is still warnings even if you already fix what should be fixed, you have to run `git commit --no-verify` to bypass the hook.