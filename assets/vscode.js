// vscode.js -- adds an "open in VS Code" link after every link to a .cpp or .h
// file on a lab page, so the file opens in VS Code attached to the course container.
//
// The link is  vscode://vscode-remote/attached-container+<hex of {"containerName":"/NAME"}>/FOLDER/LabN/PATH:1
// (tested 2026-10-10 with VS Code 1.141 + Dev Containers 0.469: VS Code asks once
// "open this folder or file?", then opens the file; without the :1 it opens a folder).
// FOLDER and NAME default to what the Pre-Lab sets up and can be changed in the
// left menu ("Open code in VS Code"); the browser remembers them.
// Paths follow the starter zip's layout, which matches the lab folders here:
// LabN/exercises/exK-.../ and LabN/examples/....
(function () {
  var DEFAULTS = { folder: '/home/cssuwbstudent/CSSSKL342', container: 'cssskl342' };
  var KEY = 'cssskl342-vscode';
  var labMatch = location.pathname.match(/\/(Lab\d+)\//);
  if (!labMatch) return;
  var lab = labMatch[1];

  function load() {
    var s = {};
    try { s = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch (e) { s = {}; }
    return { folder: s.folder || DEFAULTS.folder, container: s.container || DEFAULTS.container };
  }
  function save(s) {
    try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) { /* private window: just don't remember */ }
  }
  function hex(text) {
    var out = '';
    for (var i = 0; i < text.length; i++) out += ('0' + text.charCodeAt(i).toString(16)).slice(-2);
    return out;
  }
  function vscodeUrl(href, s) {
    var rel = href;
    var folder = s.folder.replace(/\/+$/, '');
    return 'vscode://vscode-remote/attached-container+' + hex('{"containerName":"/' + s.container + '"}') +
      folder + '/' + lab + '/' + rel + ':1';
  }

  // One small link after each source-file link.
  var sources = Array.prototype.slice.call(
    document.querySelectorAll('main a[href$=".cpp"], main a[href$=".h"]'));
  var added = sources.map(function (a) {
    var v = document.createElement('a');
    v.className = 'vsc';
    v.title = 'Open in VS Code, in your container (VS Code asks once to confirm)';
    v.textContent = 'open in VS Code';
    a.insertAdjacentText('afterend', ' ');
    a.parentNode.insertBefore(v, a.nextSibling.nextSibling);
    return { link: v, href: a.getAttribute('href') };
  });
  function refresh() {
    var s = load();
    added.forEach(function (x) { x.link.href = vscodeUrl(x.href, s); });
  }
  refresh();

  // Settings, at the bottom of the left menu.
  var nav = document.querySelector('nav.toc');
  if (!nav || !added.length) return;
  var s = load();
  var box = document.createElement('div');
  box.innerHTML =
    '<div class="label" style="margin-top:24px">VS Code links</div>' +
    '<details class="vsc-settings"><summary title="Show or hide the settings">Open code in VS Code</summary>' +
    '<div class="vsc-body">' +
    '<p>Each <span class="vsc-sample">open in VS Code</span> link opens that file in VS Code, attached to your ' +
    'container, if the file is in your container. Extract the starter zip into the folder below. ' +
    'VS Code asks whether to open the file: click <b>Yes</b>. ' +
    'Step by step, and what to check if a link does nothing: ' +
    '<a href="../Pre-Lab/index.html#fyi-vscode">Pre-Lab, For your info</a>.</p>' +
    '<label>Folder that holds your <code>' + lab + '</code> folder<input type="text" id="vsc-folder" spellcheck="false"></label>' +
    '<label>Container name<input type="text" id="vsc-container" spellcheck="false"></label>' +
    '<button type="button" id="vsc-reset">Reset to the Pre-Lab setup</button>' +
    '</div></details>';
  nav.appendChild(box);
  var folderIn = box.querySelector('#vsc-folder'), contIn = box.querySelector('#vsc-container');
  folderIn.value = s.folder;
  contIn.value = s.container;
  function onChange() {
    save({ folder: folderIn.value.trim() || DEFAULTS.folder, container: contIn.value.trim() || DEFAULTS.container });
    refresh();
  }
  folderIn.addEventListener('change', onChange);
  contIn.addEventListener('change', onChange);
  box.querySelector('#vsc-reset').addEventListener('click', function () {
    folderIn.value = DEFAULTS.folder;
    contIn.value = DEFAULTS.container;
    onChange();
  });
})();
