// gdb.js -- the gdb / debugger reference, shown on reference/gdb.html.
// Edit the list here; that page has <div id="gdb-commands-slot"></div> where it
// appears, and every lab page links to it from its left menu (Reference).
// Load this BEFORE lab.js, so the menu highlighter can find the sections.
// Every command and output shown was checked with gdb 14 in cssimages/linuxlab.
(function () {
  var slot = document.getElementById('gdb-commands-slot');
  if (!slot) return;

  function table(id, title, rows, head) {
    head = head || ['Command', 'Example', 'What it does'];
    var html = '<h3 id="' + id + '" style="margin-top:22px">' + title + '</h3>' +
      '<div class="tbl tbl-scroll"><table><thead><tr><th style="width:26%">' + head[0] + '</th>' +
      '<th style="width:30%">' + head[1] + '</th><th>' + head[2] + '</th></tr></thead><tbody>';
    rows.forEach(function (r) {
      html += '<tr><td><code>' + r[0] + '</code></td><td>' + (r[1] ? '<code>' + r[1] + '</code>' : '') + '</td><td>' + r[2] + '</td></tr>';
    });
    return html + '</tbody></table></div>';
  }

  var html = '<section id="gdb-commands"><h2>gdb command reference</h2>' +
    '<div class="callout info"><span class="title">Compile with <code>-g</code> first</span>' +
    'gdb needs <code>-g</code> to show file names, line numbers, and variable values; every Makefile in this course uses it. ' +
    'Type gdb commands at the <code>(gdb)</code> prompt. Short forms in parentheses: <code>b</code> for <code>break</code>, and so on. ' +
    'Pressing <code>Enter</code> on an empty line repeats the last command (handy for <code>next</code>). ' +
    'Inside the container gdb may print <i>warning: Error disabling address space randomization</i>: that\'s harmless.</div>';

  html += table('gdb-start', 'Start, run, and stop', [
    ['gdb <i>program</i>', 'gdb ./grades', 'Start gdb on a program. It doesn\'t run yet: set breakpoints first if you want them.'],
    ['run (r)', 'run<br>run one two &lt; in.txt', 'Run the program. Anything after <code>run</code> becomes its command-line arguments (and <code>&lt; file</code> its input), and <b>replaces</b> the arguments of earlier runs.'],
    ['Ctrl+C', '', 'Pause a running program (for example, one stuck in a loop) and return to <code>(gdb)</code>.'],
    ['kill', 'kill', 'Stop the program but stay in gdb; <code>run</code> starts it again from the beginning.'],
    ['quit (q)', 'quit', 'Leave gdb. If the program is still running, answer <code>y</code>.']
  ]);
  html += table('gdb-crash', 'After a crash', [
    ['bt', 'bt', '<b>The first thing to type.</b> Backtrace: the function where it stopped (<code>#0</code>), the line that called it (<code>#1</code>), and so on up to <code>main</code>.'],
    ['frame <i>N</i> (f)', 'frame 1', 'Switch to the caller numbered <i>N</i> in <code>bt</code>, to look at its variables.'],
    ['up / down', 'up', 'Move one caller up (toward <code>main</code>) or back down.'],
    ['list (l)', 'list<br>list 12,14', 'Show the source code around the current line, or a range of lines.']
  ]);
  html += table('gdb-break', 'Breakpoints: stop at a chosen place', [
    ['break (b)', 'break average<br>break grades.cpp:13', 'Stop when a function starts, or when a line is reached.'],
    ['tbreak', 'tbreak report', 'A one-time breakpoint: stops once, then deletes itself.'],
    ['condition', 'condition 1 avg &lt; 75', 'Make breakpoint 1 stop only when the condition is true.'],
    ['info breakpoints', 'info breakpoints', 'List breakpoints, with their numbers.'],
    ['delete', 'delete 2<br>delete', 'Delete breakpoint 2, or all of them.']
  ]);
  html += table('gdb-step', 'Step through the code', [
    ['next (n)', 'next', 'Run the current line; if it calls a function, run the whole call without stopping in it.'],
    ['step (s)', 'step', 'Run the current line, but go <i>into</i> a function it calls.'],
    ['finish', 'finish', 'Run to the end of the current function; gdb shows the value it returned.'],
    ['continue (c)', 'continue', 'Run until the next breakpoint (or the end, or a crash).'],
    ['until', 'until 30', 'Run until line 30 is reached; handy to get past the rest of a loop.']
  ]);
  html += table('gdb-look', 'Look at variables', [
    ['print (p)', 'print total<br>print total / count<br>print (double) total / count', 'Show a variable, or any C++ expression, in the current function.'],
    ['info args', 'info args', 'Show the current function\'s parameters.'],
    ['info locals', 'info locals', 'Show the current function\'s local variables.'],
    ['display', 'display avg', 'Show <code>avg</code> again every time the program stops. <code>undisplay</code> stops it.'],
    ['watch', 'watch avg', 'Stop whenever <code>avg</code> changes (while it\'s in scope).']
  ]);
  html += table('gdb-vscode', 'The same in VS Code', [
    ['continue', 'F5', 'Also starts debugging. Start a one-file program with the &#9655; menu &rarr; <b>Debug C/C++ File</b> (or the Command Palette). Needs the C/C++ extension installed <i>in the container</i>: if there is no &#9655; button, open Extensions and click <b>Install in Container</b> on <b>C/C++ Extension Pack</b>.'],
    ['next', 'F10', 'Step over.'],
    ['step', 'F11', 'Step into.'],
    ['finish', 'Shift+F11', 'Step out.'],
    ['break', 'click left of a line number', 'Toggle a breakpoint (red dot), or press <code>F9</code> on the line.'],
    ['print / info locals', 'Variables pane', 'Shows the current function\'s parameters and locals; add expressions in the <b>Watch</b> pane.'],
    ['bt / frame', 'Call Stack pane', 'Click a caller to see its variables.']
  ], ['gdb', 'VS Code', 'Notes']);
  html += '<div class="callout warn" style="margin-top:14px"><span class="title">Which tool when?</span>' +
    '<b>A crash:</b> <code>gdb ./prog</code>, <code>run</code>, <code>bt</code>, then <code>frame</code> and <code>print</code>. ' +
    '<b>Wrong output:</b> <code>break</code> where the values are still right, then <code>next</code>/<code>step</code> and <code>print</code> until one isn\'t. ' +
    'VS Code\'s debug button handles one-file programs; for programs built from several <code>.cpp</code> files (or over SSH), use gdb in the terminal.</div>';

  slot.outerHTML = html + '</section>';
})();
