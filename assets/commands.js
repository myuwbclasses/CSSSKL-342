// commands.js -- the Linux command reference, shown on reference/linux.html.
// Edit the list here; that page has <div id="linux-commands-slot"></div> where it
// appears, and every lab page links to it from its left menu (Reference).
// Load this BEFORE lab.js, so the menu highlighter can find the sections.
(function () {
  var slot = document.getElementById('linux-commands-slot');
  if (!slot) return;

  function table(id, title, rows) {
    var html = '<h3 id="' + id + '" style="margin-top:22px">' + title + '</h3>' +
      '<div class="tbl tbl-scroll"><table><thead><tr><th style="width:30%">Command</th>' +
      '<th style="width:33%">Example</th><th>What it does</th></tr></thead><tbody>';
    rows.forEach(function (r) {
      html += '<tr><td><code>' + r[0] + '</code></td><td><code>' + r[1] + '</code></td><td>' + r[2] + '</td></tr>';
    });
    return html + '</tbody></table></div>';
  }

  var html = '<section id="linux-commands"><h2>Linux command reference</h2>' +
    '<div class="callout info"><span class="title">Type these in VS Code\'s terminal, attached to your container</span>' +
    'The prompt looks like <code>[cssuwbstudent@cssskl342 CSSSKL342]$</code>. Lab 1 Part 0 (the warm-up and practice) introduces the everyday ones. ' +
    'The image has no manual pages: use <code>--help</code> instead, for example <code>ls --help</code>.</div>';

  html += table('cmd-move', 'Where am I? Moving around', [
    ['pwd', 'pwd', 'Print the full path of the current folder.'],
    ['ls', 'ls<br>ls -l<br>ls -a<br>ls -R', 'List the current folder. <code>-l</code> adds sizes and dates, <code>-a</code> shows hidden names (starting with <code>.</code>), <code>-R</code> lists every folder inside too.'],
    ['cd <i>folder</i>', 'cd part0<br>cd ..<br>cd ~<br>cd -', 'Change the current folder: into <code>part0</code>, up one level, to your home folder, back to where you just were.']
  ]);
  html += table('cmd-files', 'Files and folders', [
    ['mkdir <i>folder</i>', 'mkdir backup<br>mkdir -p part0/warmup', 'Make a folder. <code>-p</code> also makes any missing folders on the way, and doesn\'t complain if it exists.'],
    ['touch <i>file</i>', 'touch empty.txt', 'Make an empty file (or update an existing file\'s time).'],
    ['cp <i>from to</i>', 'cp notes.txt copy.txt<br>cp -r Lab1 Lab1-backup', 'Copy a file. <code>-r</code> copies a whole folder.'],
    ['mv <i>from to</i>', 'mv empty.txt blank.txt<br>mv copy.txt backup/', 'Rename, or move into a folder. Same command for both.'],
    ['rm <i>file</i>', 'rm blank.txt<br>rm -r warmup', 'Delete a file. <code>-r</code> deletes a folder and everything in it. <b>There is no Recycle Bin: it is gone.</b> Run <code>pwd</code> first.'],
    ['rmdir <i>folder</i>', 'rmdir backup', 'Delete an <i>empty</i> folder; refuses if anything is inside (<code>Directory not empty</code>). Safer than <code>rm -r</code>.']
  ]);
  html += table('cmd-view', 'Looking at and writing text', [
    ['cat <i>file</i>', 'cat notes.txt', 'Print a whole file.'],
    ['less <i>file</i>', 'less limits.cpp', 'Page through a long file: Space for the next page, <code>/word</code> to search, <code>q</code> to quit.'],
    ['echo <i>text</i>', 'echo "first line" &gt; notes.txt<br>echo "second line" &gt;&gt; notes.txt', 'Print text. <code>&gt;</code> sends it into a file, replacing what was there; <code>&gt;&gt;</code> adds it to the end.']
  ]);
  html += table('cmd-help', 'Help and the screen', [
    ['<i>command</i> --help', 'ls --help', 'Show a command\'s options.'],
    ['clear', 'clear', 'Clear the terminal screen (or press <code>Ctrl+L</code>).']
  ]);

  html += '<h3 id="cmd-keys" style="margin-top:22px">Keys that save time</h3><div class="tbl tbl-scroll"><table><tbody>' +
    '<tr><td style="width:30%"><code>Tab</code></td><td>Finish a file or folder name for you: type <code>cd pa</code> and press Tab. Press it twice to see the choices.</td></tr>' +
    '<tr><td><code>&uarr;</code> / <code>&darr;</code></td><td>Bring back earlier commands, to run again or edit.</td></tr>' +
    '<tr><td><code>Ctrl+C</code></td><td>Stop the running program (for example, one stuck in a loop).</td></tr>' +
    '<tr><td><code>Ctrl+L</code></td><td>Clear the screen, like <code>clear</code>.</td></tr>' +
    '</tbody></table></div>';

  html += table('cmd-course', 'Also used in this course', [
    ['g++', 'g++ -std=c++17 -Wall -Wextra hello.cpp -o hello', 'Compile and link a program, with the warnings we always turn on.'],
    ['./<i>program</i>', './hello', 'Run a program in the current folder (Linux needs the <code>./</code>).'],
    ['make', 'make<br>make clean', 'Build with the folder\'s <code>Makefile</code>; <code>make clean</code> deletes what it built.'],
    ['docker', 'docker start cssskl342<br>docker ps', 'In PowerShell or the Mac Terminal (not inside Linux): start your container; list running containers.']
  ]);

  slot.outerHTML = html + '</section>';
})();
