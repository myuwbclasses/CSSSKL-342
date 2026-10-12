"""Collects the instructor's example programs that fit each lab, for the instructor's own use.

Source: the private repo's MyOwnExamples (sibling folder CSSSKL-342-MyOwn; the originals stay there, unchanged).
For each lab in EXAMPLES below, this script rebuilds
    <MyOwnExamples>/LabN-examples/<name>/   (with a README.txt)
    <MyOwnExamples>/LabN-examples.zip
Both stay in the PRIVATE repo: nothing is written into the published
CSS342-New lab folders, and the lab pages and slides do not mention the examples
(instructor decision, 2026-10-10). Use them in class as demos if you like.

Run after changing EXAMPLES or an example:   python make_examples.py
"""
import os
import shutil
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
SRC = os.path.normpath(os.path.join(ROOT, "..", "CSSSKL-342-MyOwn", "zOld_Before_AI (Pre_Oct_2026)", "MyOwnExamples"))
FIXED_TIME = (2026, 1, 1, 0, 0, 0)
KEEP = (".cpp", ".h", ".txt")

# lab -> list of (folder name, source folder under MyOwnExamples, part, what to look for)
EXAMPLES = {
    2: [
        ("01-cerr-cout", "After_Lab1/2.CerrCout", 1,
         "Where did the cout message go? Run it, then uncomment #define CERR and run it again. "
         "It crashes on purpose, at the last line."),
        ("02-reading-compiler-errors", "After_Lab1/6.HowToParseCompilerErrors", 1,
         "Doesn't compile, on purpose. Read the FIRST error, fix only that, recompile; repeat."),
        ("03-struct-vs-class", "After_Lab1/4.StructVsClass", 2,
         "A struct is a class whose members are public by default. Objects without new."),
        ("04-const-members", "After_Lab3/Lab4_Explain/4.Consts", 2,
         "What a const member function, a const & parameter, and a const & return each forbid. "
         "Uncomment the illegal lines one at a time and read the errors."),
        ("05-constructor-destructor-messages", "After_Lab2/Lab3_Explain/2.Class+Operator", 3,
         "A class whose constructors and destructor print: match each line to the code. "
         "It also defines operator++ as a global function (Part 4)."),
        ("06-operator-plusplus-as-member", "After_Lab2/Lab3_Explain/3.Operator++AsAMethod", 4,
         "The same operator++ written as a member: ++a and a.operator++() are the same call."),
        ("07-member-vs-global-operators", "After_Lab3/2.Operator", 4,
         "operator+ as a member, operator- as a global, and operator<< as a friend, each called both ways."),
        ("08-return-a-reference", "After_Lab2/Lab3_Explain/6.ReturnReference", 4,
         "anObj.getA() = 10; works because getA returns int&. Also a friend operator<< and chaining."),
        ("09-prefix-postfix-int", "After_Lab2/Lab3_Explain/7.PrePost-Fix-FirstTry", 4,
         "++j vs. i++ on plain ints: which value does the expression have?"),
        ("10-prefix-postfix-operators", "After_Lab3/6.Pre-PostFix", 4,
         "Writing both ++ operators for a class: the prefix returns *this by reference, "
         "the postfix (with the unused int) returns the old value by value."),
        ("11-nested-struct-and-operator", "After_Lab4/1.Struct-And-Operator", 4,
         "A struct declared inside a class, and two friend operator<< functions: which one does cout << call?"),
    ],
}

README_HEAD = """Lab {n} -- instructor examples

Small programs from your instructor, each showing one idea from the lab. They are
optional: try them while you study, or when you finish an exercise early.

To build and run one, in VS Code's terminal attached to your container:
    cd ~/CSSSKL342/Lab{n}-examples/<folder>
    g++ -std=c++17 -Wall -Wextra *.cpp -o demo && ./demo
Some print warnings (an unused variable, say); that's fine. Examples that fail to
compile or crash on purpose say so below.

"""

for n, items in EXAMPLES.items():
    assert all(not src.startswith(f"Lab{n}-examples") for _, src, _, _ in items)
    out_dir = os.path.join(SRC, f"Lab{n}-examples")
    if os.path.isdir(out_dir):
        shutil.rmtree(out_dir)
    os.makedirs(out_dir)
    readme = README_HEAD.format(n=n)
    count = 0
    for name, src, part, what in items:
        src_dir = os.path.join(SRC, *src.split("/"))
        dest = os.path.join(out_dir, name)
        os.makedirs(dest)
        for f in sorted(os.listdir(src_dir)):
            p = os.path.join(src_dir, f)
            if os.path.isfile(p) and f.endswith(KEEP):
                shutil.copy2(p, os.path.join(dest, f))
                count += 1
        readme += f"{name}  (Part {part})\n    {what}\n\n"
    with open(os.path.join(out_dir, "README.txt"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(readme)
    zpath = os.path.join(SRC, f"Lab{n}-examples.zip")
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for d, dirs, files in os.walk(out_dir):
            dirs.sort()
            for f in sorted(files):
                p = os.path.join(d, f)
                arc = f"Lab{n}-examples/" + os.path.relpath(p, out_dir).replace(os.sep, "/")
                info = zipfile.ZipInfo(arc, FIXED_TIME)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                with open(p, "rb") as fh:
                    z.writestr(info, fh.read())
    print(f"Lab{n}: {len(items)} examples, {count} files -> {zpath}")
