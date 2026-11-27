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
      if (mode === 'rank') {
        const rA = parseInt(a.getAttribute('data-rank') || '99') || 99;
        const rB = parseInt(b.getAttribute('data-rank') || '99') || 99;
        return rA - rB;
      } else if (mode === 'unit') {
        const uA = parseInt((a.getAttribute('data-unit') || 'u0').replace('u', '')) || 0;
        const uB = parseInt((b.getAttribute('data-unit') || 'u0').replace('u', '')) || 0;
        if (uA !== uB) return uA - uB;
        const midA = a.getAttribute('data-mid') === 'mid1' ? 1 : 2;
        const midB = b.getAttribute('data-mid') === 'mid1' ? 1 : 2;
        if (midA !== midB) return midA - midB;
        const qA = parseInt(a.getAttribute('data-qno') || '0');
        const qB = parseInt(b.getAttribute('data-qno') || '0');
        return qA - qB;
      } else if (mode === 'marks') {
        const mA = a.getAttribute('data-marks') === '10m' ? 0 : 1;
        const mB = b.getAttribute('data-marks') === '10m' ? 0 : 1;
        if (mA !== mB) return mA - mB;
        const uA = parseInt((a.getAttribute('data-unit') || 'u0').replace('u', '')) || 0;
        const uB = parseInt((b.getAttribute('data-unit') || 'u0').replace('u', '')) || 0;
        if (uA !== uB) return uA - uB;
        return parseInt(a.getAttribute('data-qno') || '0') - parseInt(b.getAttribute('data-qno') || '0');
      } else if (mode === 'mid') {
        const midA = a.getAttribute('data-mid') === 'mid1' ? 1 : 2;
        const midB = b.getAttribute('data-mid') === 'mid1' ? 1 : 2;
        if (midA !== midB) return midA - midB;
        return parseInt(a.getAttribute('data-qno') || '0') - parseInt(b.getAttribute('data-qno') || '0');
      }
      return 0;
    });

    cards.forEach(c => container.appendChild(c));
  }

  if (sortSelect) {
    sortSelect.addEventListener('change', () => sortCards(sortSelect.value));
    sortCards(sortSelect.value || 'rank');
  }

  // --- 5. SEARCH & FILTER ENGINE ---
  const searchInput = document.getElementById('searchInput');
  const filterChips = document.querySelectorAll('.filter-chip');
  let activeFilter = 'all';

  function normalizeTier(key) {
    if (!key) return '';
    const k = String(key).toLowerCase().trim();
    if (k === 'tier1' || k === 't1' || k === '1') return 'tier1';
    if (k === 'tier2' || k === 't2' || k === '2') return 'tier2';
    if (k === 'tier3' || k === 't3' || k === '3') return 'tier3';
    if (k === 'tier4' || k === 't4' || k === '4') return 'tier4';
    return k;
  }

  window.filterByUnit = function(unitKey) {
    filterChips.forEach(c => c.classList.remove('active'));
    const targetChip = document.querySelector(`.filter-chip[data-filter="${unitKey}"]`);
    if (targetChip) {
      targetChip.classList.add('active');
      try {
        targetChip.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
      } catch (e) {}
    }
    activeFilter = unitKey;

    // Highlight active unit hub card if any
    document.querySelectorAll('.unit-hub-card').forEach(c => c.classList.remove('active-unit-card'));
    const hubCard = document.querySelector(`.unit-hub-card[onclick*="'${unitKey}'"]`);
    if (hubCard) hubCard.classList.add('active-unit-card');

    // Remove active tier card highlight
    document.querySelectorAll('.tier-summary-card').forEach(c => c.classList.remove('active-tier-card'));

    // Auto-sort into natural question sequence if a unit or mid filter is chosen
    if (unitKey.startsWith('u') || unitKey === 'mid1' || unitKey === 'mid2') {
      if (sortSelect) sortSelect.value = 'unit';
      sortCards('unit');
    }

    applyFilters();
  };

  window.filterByTier = function(tierKey) {
    const norm = normalizeTier(tierKey);
    activeFilter = norm;

    filterChips.forEach(c => {
      const cFilter = normalizeTier(c.getAttribute('data-filter') || '');
      c.classList.toggle('active', cFilter === norm);
    });

    const targetChip = document.querySelector(`.filter-chip[data-filter="${norm}"]`);
    if (targetChip) {
      try {
        targetChip.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
      } catch (e) {}
    }

    // Highlight active tier summary card if any
    document.querySelectorAll('.tier-summary-card').forEach(c => c.classList.remove('active-tier-card'));
    const cardMap = { 'tier1': 't1', 'tier2': 't2', 'tier3': 't3', 'tier4': 't4' };
    if (cardMap[norm]) {
      const tCard = document.querySelector(`.tier-summary-card.${cardMap[norm]}`);
      if (tCard) tCard.classList.add('active-tier-card');
    }

    // Remove active unit card highlight
    document.querySelectorAll('.unit-hub-card').forEach(c => c.classList.remove('active-unit-card'));

    // Auto-sort to rank 1-40 order whenever a tier or fasttrack is selected
    if (norm === 'fasttrack' || norm.startsWith('tier')) {
      if (sortSelect) sortSelect.value = 'rank';
      sortCards('rank');
    }

    applyFilters();
  };

  filterChips.forEach(chip => {
    chip.addEventListener('click', () => {
      const rawFilter = chip.getAttribute('data-filter');
      if (!rawFilter) return;

      const norm = normalizeTier(rawFilter);
      activeFilter = norm;

      filterChips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');

      // Highlight active unit hub card if any
      document.querySelectorAll('.unit-hub-card').forEach(c => c.classList.remove('active-unit-card'));
      const hubCard = document.querySelector(`.unit-hub-card[onclick*="'${activeFilter}'"]`);
      if (hubCard) hubCard.classList.add('active-unit-card');

      // Highlight active tier card if any
      document.querySelectorAll('.tier-summary-card').forEach(c => c.classList.remove('active-tier-card'));
      const cardMap = { 'tier1': 't1', 'tier2': 't2', 'tier3': 't3', 'tier4': 't4' };
      if (cardMap[activeFilter]) {
        const tCard = document.querySelector(`.tier-summary-card.${cardMap[activeFilter]}`);
        if (tCard) tCard.classList.add('active-tier-card');
      }

      // Auto-sort to rank if fasttrack or tier chosen
      if (activeFilter === 'fasttrack' || activeFilter.startsWith('tier')) {
        if (sortSelect) sortSelect.value = 'rank';
        sortCards('rank');
      } else if (activeFilter.startsWith('u') || activeFilter === 'mid1' || activeFilter === 'mid2') {
        if (sortSelect) sortSelect.value = 'unit';
        sortCards('unit');
      }

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
      const cardTier = normalizeTier(card.getAttribute('data-tier') || '');
      const text = card.textContent.toLowerCase();

      let matchesFilter = false;
      if (activeFilter === 'all' || activeFilter === 'fasttrack' || activeFilter === 'keypoints') {
        matchesFilter = true;
      } else if (activeFilter.startsWith('tier') && cardTier === activeFilter) {
        matchesFilter = true;
      } else if (activeFilter === 'mid1' && mid === 'mid1') {
        matchesFilter = true;
      } else if (activeFilter === 'mid2' && mid === 'mid2') {
        matchesFilter = true;
      } else if (activeFilter === '5m' && marks === '5m') {
        matchesFilter = true;
      } else if (activeFilter === '10m' && marks === '10m') {
        matchesFilter = true;
      } else if (activeFilter === unit) {
        matchesFilter = true;
      }

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

  // --- 6. UNIFIED AUDIO & LO-FI LOUNGE ENGINE ---
  const audioPlayBtn = document.getElementById('audioPlayBtn');
  const audioModeSelect = document.getElementById('audioModeSelect');
  const audioVolSlider = document.getElementById('audioVolSlider');
  const ambientVinylBtn = document.getElementById('ambientVinylBtn');
  const ambientRainBtn = document.getElementById('ambientRainBtn');
  const audioStatusPill = document.getElementById('audioStatusPill');
  const audioEqBars = document.getElementById('audioEqBars');

  // --- 7. YOUTUBE LO-FI VISUAL LOUNGE ---
  const ytLoungeToggleBtn = document.getElementById('ytLoungeToggleBtn');
  const ytMiniPlayer = document.getElementById('ytMiniPlayer');
  const ytMiniCloseBtn = document.getElementById('ytMiniCloseBtn');
  const ytIframe = document.getElementById('ytIframe');
  const ytCurrentTitle = document.getElementById('ytCurrentTitle');
  const ytChips = document.querySelectorAll('.yt-chip');

  let currentYtVid = 'akD85MNgOFU';
  let isYtPlaying = false;

  function switchYtStream(vid, title) {
    if (!ytIframe) return;
    currentYtVid = vid;
    ytIframe.src = `https://www.youtube-nocookie.com/embed/${vid}?autoplay=1&enablejsapi=1`;
    isYtPlaying = true;
    if (ytCurrentTitle) ytCurrentTitle.textContent = `📺 ${title}`;

    // Sync dropdown selection
    if (audioModeSelect) {
      const opt = audioModeSelect.querySelector(`option[value="yt_${vid}"]`);
      if (opt) audioModeSelect.value = `yt_${vid}`;
    }

    // Sync active chip
    if (ytChips) {
      ytChips.forEach(c => c.classList.toggle('active', c.getAttribute('data-vid') === vid));
    }

    // Stop native sound generators
    if (window.studyAudio && window.studyAudio.isPlaying) {
      window.studyAudio.stop();
    }

    // Update play button & status
    if (audioPlayBtn) {
      audioPlayBtn.classList.add('playing');
      audioPlayBtn.textContent = '❚❚';
    }
    if (audioStatusPill) {
      audioStatusPill.textContent = '🔴 Live';
      audioStatusPill.className = 'audio-status-pill live';
    }
    if (audioEqBars) {
      audioEqBars.classList.add('active');
    }
  }

  function pauseYtStream() {
    if (ytIframe && ytIframe.contentWindow) {
      ytIframe.contentWindow.postMessage('{"event":"command","func":"pauseVideo","args":""}', '*');
    }
    isYtPlaying = false;
    if (audioPlayBtn) {
      audioPlayBtn.classList.remove('playing');
      audioPlayBtn.textContent = '▶';
    }
    if (audioStatusPill) {
      audioStatusPill.textContent = 'Paused';
      audioStatusPill.className = 'audio-status-pill';
    }
    if (audioEqBars) {
      audioEqBars.classList.remove('active');
    }
  }

  function playYtStream() {
    if (!ytIframe.src || !ytIframe.src.includes(currentYtVid)) {
      const title = audioModeSelect?.selectedOptions[0]?.text || 'Zelda BOTW OST';
      switchYtStream(currentYtVid, title);
    } else {
      if (ytIframe && ytIframe.contentWindow) {
        ytIframe.contentWindow.postMessage('{"event":"command","func":"playVideo","args":""}', '*');
      }
      isYtPlaying = true;
      if (audioPlayBtn) {
        audioPlayBtn.classList.add('playing');
        audioPlayBtn.textContent = '❚❚';
      }
      if (audioStatusPill) {
        audioStatusPill.textContent = '🔴 Live';
        audioStatusPill.className = 'audio-status-pill live';
      }
      if (audioEqBars) {
        audioEqBars.classList.add('active');
      }
    }
  }

  if (audioPlayBtn) {
    audioPlayBtn.addEventListener('click', () => {
      const mode = audioModeSelect ? audioModeSelect.value : 'yt_akD85MNgOFU';
      if (mode.startsWith('yt_')) {
        if (isYtPlaying) {
          pauseYtStream();
        } else {
          playYtStream();
        }
      } else {
        if (!window.studyAudio) return;
        const isPlaying = window.studyAudio.togglePlay();
        audioPlayBtn.classList.toggle('playing', isPlaying);
        audioPlayBtn.textContent = isPlaying ? '❚❚' : '▶';
      }
    });
  }

  if (audioModeSelect) {
    audioModeSelect.addEventListener('change', (e) => {
      const mode = e.target.value;
      if (mode.startsWith('yt_')) {
        const vid = mode.replace('yt_', '');
        const title = e.target.selectedOptions[0]?.text || 'Lo-Fi Stream';
        switchYtStream(vid, title);
        if (ytMiniPlayer) ytMiniPlayer.classList.add('show');
        if (ytLoungeToggleBtn) ytLoungeToggleBtn.classList.add('active');
      } else {
        pauseYtStream();
        if (window.studyAudio) {
          window.studyAudio.setMode(mode);
          if (!window.studyAudio.isPlaying) {
            window.studyAudio.start();
          }
          if (audioPlayBtn) {
            audioPlayBtn.classList.add('playing');
            audioPlayBtn.textContent = '❚❚';
          }
        }
      }
    });
  }

  if (audioVolSlider) {
    audioVolSlider.addEventListener('input', (e) => {
      const val = parseFloat(e.target.value);
      if (window.studyAudio) {
        window.studyAudio.setVolume(val);
      }
      if (ytIframe && ytIframe.contentWindow) {
        ytIframe.contentWindow.postMessage('{"event":"command","func":"setVolume","args":[' + Math.round(val * 100) + ']}', '*');
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

  if (ytLoungeToggleBtn && ytMiniPlayer) {
    ytLoungeToggleBtn.addEventListener('click', () => {
      const isShowing = ytMiniPlayer.classList.toggle('show');
      ytLoungeToggleBtn.classList.toggle('active', isShowing);
      if (isShowing) {
        if (!ytIframe.src || ytIframe.src === '' || ytIframe.src === window.location.href) {
          const mode = audioModeSelect ? audioModeSelect.value : 'yt_akD85MNgOFU';
          const vid = mode.startsWith('yt_') ? mode.replace('yt_', '') : 'akD85MNgOFU';
          const title = audioModeSelect?.selectedOptions[0]?.text || 'Zelda BOTW — Full Original Soundtrack (OST)';
          switchYtStream(vid, title);
        }
      }
    });
  }

  if (ytMiniCloseBtn && ytMiniPlayer) {
    ytMiniCloseBtn.addEventListener('click', () => {
      ytMiniPlayer.classList.remove('show');
      if (ytLoungeToggleBtn) ytLoungeToggleBtn.classList.remove('active');
    });
  }

  if (ytChips) {
    ytChips.forEach(chip => {
      chip.addEventListener('click', () => {
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
