# AutomationWorks
Journey of Automation

For this journey we will use <code> #!/usr/bin/env python3 </code>

We start with "Modules" as these are important components of code reuse concept. The modules are basically collection of .py files. The python files inside of a modules contain different functions. These functions can be called using the module name and . or dot notation followed by the function name.

One thing to remember, to use the module to be recognised by an interpreter we need to include <code>" __init__.py "</code> file. 

Lets write some basic script to check disk usage and cpu usage. Preview the <code> disk_cpu.py </code> file.

<lots to add>

diff and patch Cheat Sheet
diff
diff is used to find differences between two files. On its own, it’s a bit hard to use; instead, use it with diff -u to find lines which differ in two files:

diff -u
diff -u is used to compare two files, line by line, and have the differing lines compared side-by-side in the same output. See below:


~$ cat menu1.txt 
Menu1:

Apples
Bananas
Oranges
Pears

~$ cat menu2.txt 
Menu:

Apples
Bananas
Grapes
Strawberries

~$ diff -u menu1.txt menu2.txt 
--- menu1.txt   2019-12-16 18:46:13.794879924 +0900
+++ menu2.txt   2019-12-16 18:46:42.090995670 +0900
@@ -1,6 +1,6 @@
-Menu1:
+Menu:
 
 Apples
 Bananas
-Oranges
-Pears
+Grapes
+Strawberries

Patch
Patch is useful for applying file differences. See the below example, which compares two files. The comparison is saved as a .diff file, which is then patched to the original file!

~$ cat hello_world.txt 
Hello World
~$ cat hello_world_long.txt 
Hello World

It's a wonderful day!
~$ diff -u hello_world.txt hello_world_long.txt 
--- hello_world.txt     2019-12-16 19:24:12.556102821 +0900
+++ hello_world_long.txt        2019-12-16 19:24:38.944207773 +0900
@@ -1 +1,3 @@
 Hello World
+
+It's a wonderful day!
~$ diff -u hello_world.txt hello_world_long.txt > hello_world.diff
~$ patch < hello_world.diff 
patching file hello_world.txt
~$ cat hello_world.txt 
Hello World

It's a wonderful day!
