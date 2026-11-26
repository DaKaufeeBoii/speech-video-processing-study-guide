// Speech & Video Processing Master Handbook - Application & Interactivity Engine
// Handles search, sorting, multi-tier filtering, accordion toggles, audio wiring, and YouTube lounge.

document.addEventListener('DOMContentLoaded', () => {
  // --- 1. ACCORDION EXPAND / COLLAPSE ---
  window.toggleCard = function(id) {
    const body = document.getElementById('body-' + id);
    const header = document.querySelector('#' + id + ' .card-header');
    if (body) body.classList.toggle('open');
    if (header) header.classList.toggle('open');
  };

  const expandToggleBtn = document.getElementById('expandToggle');
  const toggleAllBtn = document.getElementById('toggleAllBtn');
  let isAllOpen = false;

  function setAllCardsExpanded(expanded) {
    isAllOpen = expanded;
    document.querySelectorAll('.card-body').forEach(b => {
      if (expanded) b.classList.add('open');
      else b.classList.remove('open');
    });
    document.querySelectorAll('.card-header').forEach(h => {
      if (expanded) h.classList.add('open');
      else h.classList.remove('open');
    });

    if (expandToggleBtn) {
      expandToggleBtn.textContent = expanded ? '📕 Collapse All' : '📖 Expand All';
      expandToggleBtn.classList.toggle('active-mode', expanded);
    }
    if (toggleAllBtn) {
      toggleAllBtn.textContent = expanded ? 'Collapse All' : 'Expand All';
    }
  }

  if (expandToggleBtn) {
    expandToggleBtn.addEventListener('click', () => setAllCardsExpanded(!isAllOpen));
  }
  if (toggleAllBtn) {
    toggleAllBtn.addEventListener('click', () => setAllCardsExpanded(!isAllOpen));
  }

  // --- 2. FLASHCARD & PUNCHLINE MODE ---
  const modeToggle = document.getElementById('modeToggle');
  if (modeToggle) {
    modeToggle.addEventListener('click', () => {
      document.body.classList.toggle('flashcard-mode');
      const isFc = document.body.classList.contains('flashcard-mode');
      if (isFc) {
        modeToggle.textContent = '📖 Full View';
        modeToggle.style.background = 'var(--accent)';
        modeToggle.style.color = '#fff';
        document.querySelectorAll('.card-body').forEach(b => b.classList.add('open'));
      } else {
        modeToggle.textContent = '⚡ Punchlines';
        modeToggle.style.background = 'var(--surface)';
        modeToggle.style.color = 'var(--text)';
      }
    });
  }

  // --- 3. THEME TOGGLER (DARK / LIGHT WITH PERSISTENCE) ---
  const themeToggle = document.getElementById('themeToggle');
  const savedTheme = localStorage.getItem('rs_gis_theme') || 'dark';
  document.documentElement.setAttribute('data-theme', savedTheme);

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'light' ? 'dark' : 'light';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('rs_gis_theme', next);
    });
  }

  // --- 4. SORTING ENGINE ---
  const container = document.getElementById('questionsContainer');
  const sortSelect = document.getElementById('sortSelect');

  function sortCards(mode) {
    if (!container) return;
    const cards = Array.from(container.children);
    cards.sort((a, b) => {
      if (mode === 'priority') {
        return parseInt(a.getAttribute('data-rank') || '99') - parseInt(b.getAttribute('data-rank') || '99');
      } else if (mode === 'unit') {
        return (a.getAttribute('data-orig') || '').localeCompare(b.getAttribute('data-orig') || '');
      } else if (mode === 'marks') {
        const mA = a.getAttribute('data-marks') === '10m' ? 0 : 1;
        const mB = b.getAttribute('data-marks') === '10m' ? 0 : 1;
        if (mA !== mB) return mA - mB;
        return parseInt(a.getAttribute('data-rank') || '99') - parseInt(b.getAttribute('data-rank') || '99');
      } else if (mode === 'fastest') {
        const tA = parseInt(a.getAttribute('data-time') || '10');
        const tB = parseInt(b.getAttribute('data-time') || '10');
        if (tA !== tB) return tA - tB;
        return parseInt(a.getAttribute('data-rank') || '99') - parseInt(b.getAttribute('data-rank') || '99');
      }
      return 0;
    });

    cards.forEach(c => container.appendChild(c));
  }

  if (sortSelect) {
    sortSelect.addEventListener('change', () => sortCards(sortSelect.value));
    sortCards(sortSelect.value || 'priority');
  }

  // --- 5. SEARCH & FILTER ENGINE ---
  const searchInput = document.getElementById('searchInput');
  const filterChips = document.querySelectorAll('.filter-chip');
  let activeFilter = 'all';

  window.filterByTier = function(tier) {
    filterChips.forEach(c => c.classList.remove('active'));
    const targetChip = document.querySelector(`.filter-chip[data-filter="${tier}"]`);
    if (targetChip) targetChip.classList.add('active');
    activeFilter = tier;
    applyFilters();
  };

  filterChips.forEach(chip => {
    chip.addEventListener('click', () => {
      filterChips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      activeFilter = chip.getAttribute('data-filter') || 'all';
      applyFilters();
    });
  });

  if (searchInput) {
    searchInput.addEventListener('input', applyFilters);
  }

  function applyFilters() {
    const query = searchInput ? searchInput.value.toLowerCase().trim() : '';
    const cards = document.querySelectorAll('.question-card');
    let count = 0;

    if (activeFilter === 'keypoints') {
      document.body.classList.add('keypoints-mode');
    } else {
      document.body.classList.remove('keypoints-mode');
    }

    cards.forEach(card => {
      const mid = card.getAttribute('data-mid');
      const unit = card.getAttribute('data-unit');
      const marks = card.getAttribute('data-marks');
      const tier = card.getAttribute('data-tier');
      const text = card.textContent.toLowerCase();

      let matchesFilter = false;
      if (activeFilter === 'all' || activeFilter === 'keypoints') matchesFilter = true;
      else if (activeFilter === 'important' && card.getAttribute('data-important') === 'yes') matchesFilter = true;
      else if (activeFilter === 'tier1' && tier === 'tier1') matchesFilter = true;
      else if (activeFilter === 'tier2' && tier === 'tier2') matchesFilter = true;
      else if (activeFilter === 'tier3' && tier === 'tier3') matchesFilter = true;
      else if (activeFilter === 'tier4' && tier === 'tier4') matchesFilter = true;
      else if (activeFilter === 'mid1' && mid === 'mid1') matchesFilter = true;
      else if (activeFilter === 'mid2' && mid === 'mid2') matchesFilter = true;
      else if (activeFilter === '5m' && marks === '5m') matchesFilter = true;
      else if (activeFilter === '10m' && marks === '10m') matchesFilter = true;
      else if (activeFilter === unit) matchesFilter = true;

      const matchesQuery = !query || text.includes(query);

      if (matchesFilter && matchesQuery) {
        card.style.display = 'block';
        count++;
      } else {
        card.style.display = 'none';
      }
    });

    const visibleCount = document.getElementById('visibleCount');
    if (visibleCount) visibleCount.textContent = count;
  }

  // --- 6. AUDIO CONTROLS WIRING ---
  const audioPlayBtn = document.getElementById('audioPlayBtn');
  const audioModeSelect = document.getElementById('audioModeSelect');
  const audioVolSlider = document.getElementById('audioVolSlider');
  const ambientVinylBtn = document.getElementById('ambientVinylBtn');
  const ambientRainBtn = document.getElementById('ambientRainBtn');

  if (audioPlayBtn) {
    audioPlayBtn.addEventListener('click', () => {
      if (!window.studyAudio) return;
      const isPlaying = window.studyAudio.togglePlay();
      audioPlayBtn.classList.toggle('playing', isPlaying);
      audioPlayBtn.textContent = isPlaying ? '❚❚' : '▶';
    });
  }

  if (audioModeSelect) {
    audioModeSelect.addEventListener('change', (e) => {
      if (window.studyAudio) {
        window.studyAudio.setMode(e.target.value);
      }
    });
  }

  if (audioVolSlider) {
    audioVolSlider.addEventListener('input', (e) => {
      if (window.studyAudio) {
        window.studyAudio.setVolume(parseFloat(e.target.value));
      }
    });
  }

  if (ambientVinylBtn) {
    ambientVinylBtn.addEventListener('click', () => {
      if (window.studyAudio) {
        const active = window.studyAudio.toggleVinyl();
        ambientVinylBtn.classList.toggle('active', active);
      }
    });
  }

  if (ambientRainBtn) {
    ambientRainBtn.addEventListener('click', () => {
      if (window.studyAudio) {
        const active = window.studyAudio.toggleRain();
        ambientRainBtn.classList.toggle('active', active);
      }
    });
  }

  // --- 7. YOUTUBE LO-FI VISUAL LOUNGE ---
  const ytLoungeToggleBtn = document.getElementById('ytLoungeToggleBtn');
  const ytMiniPlayer = document.getElementById('ytMiniPlayer');
  const ytMiniCloseBtn = document.getElementById('ytMiniCloseBtn');
  const ytIframe = document.getElementById('ytIframe');
  const ytCurrentTitle = document.getElementById('ytCurrentTitle');
  const ytChips = document.querySelectorAll('.yt-chip');

  function switchYtStream(vid, title) {
    if (!ytIframe) return;
    ytIframe.src = `https://www.youtube-nocookie.com/embed/${vid}?autoplay=1&enablejsapi=1`;
    if (ytCurrentTitle) ytCurrentTitle.textContent = `📺 ${title}`;
    if (window.studyAudio && window.studyAudio.isPlaying) {
      window.studyAudio.stop();
      if (audioPlayBtn) {
        audioPlayBtn.classList.remove('playing');
        audioPlayBtn.textContent = '▶';
      }
    }
  }

  if (ytLoungeToggleBtn && ytMiniPlayer) {
    ytLoungeToggleBtn.addEventListener('click', () => {
      const isShowing = ytMiniPlayer.classList.toggle('show');
      ytLoungeToggleBtn.classList.toggle('active', isShowing);
      if (isShowing) {
        if (!ytIframe.src || ytIframe.src === '' || ytIframe.src === window.location.href) {
          switchYtStream('5qap5aO4i9A', 'Lofi Girl — 24/7 Study Beats');
        }
      } else {
        if (ytIframe) ytIframe.src = "";
      }
    });
  }

  if (ytMiniCloseBtn && ytMiniPlayer) {
    ytMiniCloseBtn.addEventListener('click', () => {
      ytMiniPlayer.classList.remove('show');
      if (ytLoungeToggleBtn) ytLoungeToggleBtn.classList.remove('active');
      if (ytIframe) ytIframe.src = "";
    });
  }

  if (ytChips) {
    ytChips.forEach(chip => {
      chip.addEventListener('click', () => {
        ytChips.forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        const vid = chip.getAttribute('data-vid');
        const title = chip.getAttribute('data-title') || 'YouTube Lo-Fi';
        switchYtStream(vid, title);
      });
    });
  }

  // --- 8. FLOATING BACK TO TOP ---
  const backToTopBtn = document.getElementById('backToTopBtn');
  if (backToTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 300) {
        backToTopBtn.style.display = 'flex';
      } else {
        backToTopBtn.style.display = 'none';
      }
    }, { passive: true });

    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // --- 9. KEYBOARD SHORTCUTS ---
  window.addEventListener('keydown', (e) => {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
    
    // Space or M toggles Lo-Fi
    if (e.key === ' ' || e.code === 'Space' || e.key === 'm' || e.key === 'M') {
      e.preventDefault();
      if (audioPlayBtn) audioPlayBtn.click();
    } else if (e.key === 'Escape') {
      if (ytMiniPlayer && ytMiniPlayer.classList.contains('show')) {
        ytMiniPlayer.classList.remove('show');
        if (ytLoungeToggleBtn) ytLoungeToggleBtn.classList.remove('active');
        if (ytIframe) ytIframe.src = "";
      }
    }
  });

  // Run initial filter count
  applyFilters();
});
