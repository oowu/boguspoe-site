(function () {
  function paint(el, map, pal) {
    var cells = [];
    map.forEach(function (row) {
      row.split('').forEach(function (ch) {
        var d = document.createElement('div');
        d.style.background = pal[ch];
        d.dataset.ch = ch;
        el.appendChild(d);
        cells.push(d);
      });
    });
    return cells;
  }

  // аватар
  var skin = '#f2c39b';
  var avatarCells = paint(document.getElementById('avatar'), [
    '...HHHHHH...',
    '..HHHHHHHH..',
    '..HSSSSSSH..',
    '..SKKSSKKS..',
    '..SSSSSSSS..',
    '..SSESSESS..',
    '...SSMMSS...',
    '..BBBBBBBB..',
    '.BBBBBBBBBB.',
    '.SBBBBBBBBS.',
    '..LL....LL..',
    '.WWW....WWW.'
  ], { '.': 'transparent', H: '#3b2416', K: '#0d0d0d', S: skin, E: '#1a1c2c', M: '#b13e53', B: '#1f2a5c', L: '#1a1c2c', W: '#f4f4f4' });

  // моргание
  var eyes = avatarCells.filter(function (c) { return c.dataset.ch === 'E'; });
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduce) {
    setInterval(function () {
      eyes.forEach(function (c) { c.style.background = skin; });
      setTimeout(function () { eyes.forEach(function (c) { c.style.background = '#1a1c2c'; }); }, 160);
    }, 3200);
  }

  // слайм
  paint(document.getElementById('slime'), ['..GGGG..', '.GGGGGG.', 'GGEGGEGG', 'GGGGGGGG'],
    { '.': 'transparent', G: '#a7f070', E: '#1a1c2c' });

  // звёзды
  var stars = document.getElementById('stars');
  var colors = ['#f4f4f4', '#ffcd75', '#73eff7', '#a7f070'];
  var seed = 7;
  function rnd() { seed = (seed * 9301 + 49297) % 233280; return seed / 233280; }
  for (var i = 0; i < 28; i++) {
    var s = document.createElement('i');
    var size = rnd() > 0.7 ? 8 : 4;
    s.style.top = (rnd() * 98).toFixed(1) + '%';
    s.style.left = (rnd() * 98).toFixed(1) + '%';
    s.style.width = s.style.height = size + 'px';
    s.style.background = colors[i % 4];
    s.style.animationDuration = (1.2 + rnd() * 2).toFixed(1) + 's';
    s.style.animationDelay = (rnd() * 2).toFixed(1) + 's';
    stars.appendChild(s);
  }

  // секрет: ↑↑↓↓←→←→BA на клавиатуре или 5 быстрых тапов по аватару
  var code = ['arrowup','arrowup','arrowdown','arrowdown','arrowleft','arrowright','arrowleft','arrowright','b','a'];
  var pos = 0, busy = false;
  var shirt = avatarCells.filter(function (c) { return c.dataset.ch === 'B'; });

  function secret() {
    if (busy) return;
    busy = true;
    var page = document.querySelector('.page');
    page.classList.add('gold');
    shirt.forEach(function (c) { c.style.background = '#ffcd75'; });

    var toast = document.createElement('div');
    toast.className = 'toast';
    toast.setAttribute('role', 'status');
    toast.textContent = document.body.dataset.secret || 'SECRET FOUND! +1 UP';
    document.body.appendChild(toast);

    var rain = null;
    if (!reduce) {
      rain = document.createElement('div');
      rain.className = 'rain';
      rain.setAttribute('aria-hidden', 'true');
      for (var i = 0; i < 36; i++) {
        var c = document.createElement('i');
        c.style.left = Math.floor(Math.random() * 96) + '%';
        c.style.animationDelay = (Math.random() * 1.6).toFixed(2) + 's, 0s';
        rain.appendChild(c);
      }
      document.body.appendChild(rain);
    }

    setTimeout(function () {
      toast.remove();
      if (rain) rain.remove();
      page.classList.remove('gold');
      shirt.forEach(function (c) { c.style.background = '#1f2a5c'; });
      busy = false;
    }, 5000);
  }

  document.addEventListener('keydown', function (e) {
    var k = (e.key || '').toLowerCase();
    if (k === code[pos]) {
      pos++;
      if (pos === code.length) { pos = 0; secret(); }
    } else {
      pos = k === code[0] ? 1 : 0;
    }
  });

  var taps = [];
  document.getElementById('avatar').addEventListener('click', function () {
    var now = Date.now();
    taps = taps.filter(function (t) { return now - t < 2000; });
    taps.push(now);
    if (taps.length >= 5) { taps = []; secret(); }
  });
})();
