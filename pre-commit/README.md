#pre-commit hook

##Installation
1. make sure python 2.x get installed and be available at environment path
1. install xsrc
2. run xsrc to init your reposet
3. run `xsrc install -k pre-commit -r some-repo`
4. done

##Usage
1. This hook tests if source files are licensed under Apache or GPL, if not, will warn users and stop committing until fix it. Currently following types of source are checked out,

    '.m', '.mm', '.h', '.cpp', '.c', '.cs', '.java', '.js', '.html'
2. Because the hook cannot detect everything, when there is still warnings even if you already fix what should be fixed, you have to run `git commit -m "commit message" -n` to bypass the hook.

##License Headers
In the source folder, there are 3 license headers, which individually applies to

1. GPLv3_header -> xface specific source
2. Apachev2_polyvi_header -> owned by xface, but for where requires Apache v2
3. Apachev2_cordova_header -> modified by xface, but has to keep Apache v2, generally source files related to cordova are under this category