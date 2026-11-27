// StudyMode Audio Engine - Generative Lo-Fi & Multi-Stream Ambient System
// Based on Deep Learning StudyMode Audio Architecture (D:\Kaufee\padhai\7th-sem\Deep-Learning\StudyMode)
// Supports verified 24/7 internet Lo-Fi radio streams + generative offline Web Audio soundscapes.

class StudyAudioManager {
  constructor() {
    this.ctx = null;
    this.masterGain = null;
    this.isPlaying = false;
    this.currentMode = 'stream_chillhop'; // Default to 24/7 Live Chillhop Stream
    
    // Ambient layers
    this.vinylActive = true;
    this.rainActive = false;
    
    // Generators & nodes
    this.lofiTimer = null;
    this.currentChordProgression = 0;
    this.streamTimeout = null;
    this.rainSource = null;
    this.rainGain = null;
    this.vinylSource = null;
    this.vinylGain = null;
    this.brownSource = null;
    this.brownGain = null;
    this.binauralOscL = null;
    this.binauralOscR = null;
    this.binauralGain = null;
    
    // Online stream audio element
    this.streamAudio = new Audio();
    this.streamAudio.crossOrigin = "anonymous";
    this.streamAudio.preload = "none";
    
    // Live 24/7 Internet Radio Streams (All verified HTTPS 200 OK)
    this.streamStations = {
      'stream_chillhop': {
        name: '☕ Live: 24/7 Chillhop & Lofi',
        url: 'https://streams.ilovemusic.de/iloveradio17.mp3'
      },
      'stream_fluxfm': {
        name: '🎧 Live: FluxFM ChillHop (Berlin)',
        url: 'https://streams.fluxfm.de/Chillhop/mp3-128/streams.fluxfm.de/'
      },
      'stream_radioco': {
        name: '📻 Live: 24/7 Lo-Fi Cafe Radio',
        url: 'https://streaming.radio.co/s774887f7b/listen'
      },
      'stream_lautfm': {
        name: '🏙️ Live: Berlin Lo-Fi Lounge',
        url: 'https://lofi.stream.laut.fm/lofi'
      },
      'stream_japan': {
        name: '🌸 Live: Tokyo Lo-Fi Aesthetic',
        url: 'https://stream.zeno.fm/0r0xa792kwzuv'
      },
      'stream_anime': {
        name: '🏮 Live: Anime & Chill Lofi',
        url: 'https://stream.zeno.fm/f3wvbbqmdg8uv'
      },
      'stream_vgm_covers': {
        name: '🍄 Live: Nintendo & Game Remixes',
        url: 'https://relay.rainwave.cc/covers.mp3'
      },
      'stream_vgm_all': {
        name: '🎮 Live: Video Game Lofi & VGM',
        url: 'https://relay.rainwave.cc/all.mp3'
      },
      'stream_vgm_ocremix': {
        name: '⚔️ Live: OverClocked ReMix (VGM)',
        url: 'https://relay.rainwave.cc/ocremix.mp3'
      },
      'stream_vgm_chiptune': {
        name: '👾 Live: 8-Bit Chiptune Radio',
        url: 'https://relay.rainwave.cc/chiptune.mp3'
      },
      'stream_nightwave': {
        name: '🌌 Live: Nightwave Plaza (Vaporwave/Chill)',
        url: 'https://radio.plaza.one/mp3'
      },
      'stream_chillout': {
        name: '🍃 Live: Ambient Chillout Lounge',
        url: 'https://hirschmilch.de:7000/chillout.mp3'
      }
    };

    // YouTube Live Streams catalog for the Visual Lounge (All verified working embeds)
    this.youtubeStreams = [
      { id: 'akD85MNgOFU', title: 'Zelda BOTW — Full Original Soundtrack (OST)', icon: '🗡️' },
      { id: 'E0IvwhwQEo4', title: 'Zelda BOTW — Relaxing Field & Village Ambient OST', icon: '🍃' },
      { id: '4ykrl_VfJ_o', title: 'Zelda BOTW — Relaxing OST + Thunderstorm Ambience', icon: '🌧️' },
      { id: 'X7qeyEHuflk', title: 'Zelda BOTW — Complete 6-Hour Extended OST', icon: '🏰' },
      { id: 'nsoEPmdC-t0', title: 'Zelda BOTW — Lofi of the Wild', icon: '✨' },
      { id: 'rJlY1uKL87k', title: 'Zelda & Chill 2 — GameChops', icon: '🛡️' },
      { id: '-GAr6XkB35k', title: 'Zelda & Nintendo Piano — 24/7 Live', icon: '🌙' },
      { id: '2DVpys50LVE', title: 'Nintendo — Poké & Chill', icon: '🍄' },
      { id: 'Ac5rVi8Gg_k', title: 'Super Nintendo Lofi World — Mario & DK', icon: '🎮' },
      { id: 'h3AMUun9tHk', title: 'Video Game Study Lounge — 24/7 Live', icon: '📚' },
      { id: '5qap5aO4i9A', title: 'Lofi Girl — 24/7 Study Beats', icon: '🎧' },
      { id: '4xDzrJKXOOY', title: 'Synthwave Boy — 24/7 Live', icon: '🌆' }
    ];
    
    this.volume = 0.85;

    // Attach stream listeners
    if (this.streamAudio) {
      this.streamAudio.addEventListener('playing', () => {
        if (this.streamTimeout) clearTimeout(this.streamTimeout);
        this.updateStatus('🔴 Live', 'live');
        this.updateEqBars(true);
      });
      this.streamAudio.addEventListener('error', (e) => {
        if (this.isPlaying && this.currentMode.startsWith('stream_')) {
          console.warn("Live stream network issue, switching gracefully to offline Lo-Fi synth:", e);
          this.startOfflineFallback('🎧 Offline Backup (CORS/File)');
        }
      });
    }
  }

  updateStatus(text, className) {
    const pill = document.getElementById('audioStatusPill');
    if (pill) {
      pill.textContent = text;
      pill.className = 'audio-status-pill ' + (className || '');
    }
  }

  updateEqBars(active) {
    const eqBars = document.getElementById('audioEqBars');
    if (eqBars) {
      if (active) eqBars.classList.add('active');
      else eqBars.classList.remove('active');
    }
  }

  initContext() {
    if (!this.ctx) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) {
        this.ctx = new AudioCtx();
        this.masterGain = this.ctx.createGain();
        this.masterGain.gain.setValueAtTime(this.volume, this.ctx.currentTime);
        this.masterGain.connect(this.ctx.destination);
      }
    }
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume().catch(e => console.warn("Context resume:", e));
    }
  }

  setVolume(val) {
    this.volume = Math.max(0, Math.min(1, val));
    if (this.masterGain && this.ctx) {
      this.masterGain.gain.setTargetAtTime(this.volume, this.ctx.currentTime, 0.05);
    }
    if (this.streamAudio) {
      this.streamAudio.volume = this.volume;
    }
  }

  togglePlay() {
    this.initContext();
    if (this.isPlaying) {
      this.stop();
      this.updateStatus('Paused', '');
      return false;
    } else {
      this.start();
      return true;
    }
  }

  setMode(mode) {
    this.currentMode = mode;
    if (this.isPlaying) {
      this.stopAllGenerators();
      this.startCurrentMode();
    }
  }

  start() {
    this.initContext();
    this.isPlaying = true;
    this.startCurrentMode();
    if (this.vinylActive && (this.currentMode === 'lofi_synth' || this.currentMode.startsWith('stream_'))) {
      this.startVinyl();
    }
    if (this.rainActive) {
      this.startRain();
    }
    this.updateEqBars(true);
  }

  stop() {
    this.isPlaying = false;
    if (this.streamTimeout) {
      clearTimeout(this.streamTimeout);
      this.streamTimeout = null;
    }
    this.stopAllGenerators();
    if (this.streamAudio) {
      this.streamAudio.pause();
    }
    this.updateEqBars(false);
  }

  startCurrentMode() {
    if (this.currentMode.startsWith('yt_')) {
      return; // Handled by app.js YouTube player
    }
    if (this.currentMode.startsWith('stream_')) {
      const station = this.streamStations[this.currentMode];
      if (station) {
        this.startOnlineStream(station.url);
      } else {
        this.startOnlineStream(this.streamStations['stream_chillhop'].url);
      }
      return;
    }

    switch (this.currentMode) {
      case 'lofi_synth':
      case 'lofi_beats':
        this.updateStatus('🎹 Piano', 'live');
        this.startLofiSynth();
        break;
      case 'rain':
        this.updateStatus('🌧️ Rain', 'live');
        this.startRain(true);
        break;
      case 'binaural':
        this.updateStatus('🧠 40Hz', 'live');
        this.startBinaural();
        break;
      case 'brown_noise':
        this.updateStatus('📻 Noise', 'live');
        this.startBrownNoise();
        break;
      default:
        this.startOnlineStream(this.streamStations['stream_chillhop'].url);
        break;
    }
  }

  stopAllGenerators() {
    if (this.lofiTimer) {
      clearInterval(this.lofiTimer);
      this.lofiTimer = null;
    }
    if (this.rainSource) {
      try { this.rainSource.stop(); } catch(e) {}
      this.rainSource = null;
    }
    if (this.vinylSource) {
      try { this.vinylSource.stop(); } catch(e) {}
      this.vinylSource = null;
    }
    if (this.brownSource) {
      try { this.brownSource.stop(); } catch(e) {}
      this.brownSource = null;
    }
    if (this.binauralOscL) {
      try { this.binauralOscL.stop(); } catch(e) {}
      this.binauralOscL = null;
    }
    if (this.binauralOscR) {
      try { this.binauralOscR.stop(); } catch(e) {}
      this.binauralOscR = null;
    }
    if (this.streamAudio) {
      this.streamAudio.pause();
    }
  }

  // --- 1. ONLINE LIVE STREAM ENGINE ---
  startOnlineStream(url) {
    if (!this.streamAudio) {
      this.streamAudio = new Audio();
      this.streamAudio.crossOrigin = "anonymous";
    }
    this.stopAllGenerators();
    this.updateStatus('⏳ Connecting...', 'buffering');

    // Failsafe timer: If internet radio stream doesn't start in 4 seconds
    // (due to local file:// CORS limit, firewall, or slow ISP buffer),
    // automatically activate offline Lo-Fi synth so user NEVER gets silence!
    if (this.streamTimeout) clearTimeout(this.streamTimeout);
    this.streamTimeout = setTimeout(() => {
      if (this.isPlaying && this.currentMode.startsWith('stream_')) {
        console.warn("Live stream slow/blocked. Activating offline Lo-Fi synth backup.");
        this.startOfflineFallback('🎧 Offline Backup (Local/CORS)');
      }
    }, 4000);

    this.streamAudio.pause();
    this.streamAudio.src = url;
    this.streamAudio.volume = this.volume;
    
    const playPromise = this.streamAudio.play();
    if (playPromise !== undefined) {
      playPromise.then(() => {
        if (this.streamTimeout) clearTimeout(this.streamTimeout);
        this.updateStatus('🔴 Live', 'live');
        this.updateEqBars(true);
      }).catch(err => {
        if (this.streamTimeout) clearTimeout(this.streamTimeout);
        console.warn("Live stream playback error, falling back to offline Lo-Fi synth:", err);
        this.startOfflineFallback('🎧 Offline Backup (Local/CORS)');
      });
    }
  }

  startOfflineFallback(label = "🎧 Offline Backup") {
    if (!this.isPlaying) return;
    this.updateStatus(label, 'offline-fallback');
    this.startLofiSynth();
    if (this.vinylActive) this.startVinyl();
    this.updateEqBars(true);
  }

  // --- 2. GENERATIVE LO-FI ELECTRIC PIANO CHORDS (OFFLINE) ---
  startLofiSynth() {
    const progressions = [
      // Progression 1: Classic Neo-Soul (Dm9 -> G13 -> Cmaj9 -> Am9)
      [
        [146.83, 220.00, 261.63, 329.63, 392.00],
        [196.00, 246.94, 293.66, 329.63, 349.23],
        [130.81, 196.00, 246.94, 293.66, 329.63],
        [220.00, 261.63, 329.63, 392.00, 493.88]
      ],
      // Progression 2: Rainy Cafe (Fmaj7 -> Em7 -> Dm7 -> Cmaj7)
      [
        [174.61, 261.63, 329.63, 349.23, 440.00],
        [164.81, 246.94, 293.66, 329.63, 392.00],
        [146.83, 220.00, 261.63, 293.66, 349.23],
        [130.81, 196.00, 246.94, 329.63, 392.00]
      ],
      // Progression 3: Late Night Rhodes (Bbmaj9 -> Am7 -> Gm9 -> Fmaj9)
      [
        [116.54, 174.61, 233.08, 293.66, 349.23],
        [110.00, 164.81, 220.00, 261.63, 329.63],
        [98.00, 146.83, 196.00, 246.94, 293.66],
        [87.31, 130.81, 174.61, 220.00, 261.63]
      ],
      // Progression 4: Zelda / Nintendo Nostalgia (Cmaj7 -> Em7 -> Fmaj7 -> Gsus4)
      [
        [130.81, 196.00, 246.94, 329.63, 392.00],
        [164.81, 246.94, 293.66, 329.63, 392.00],
        [174.61, 261.63, 329.63, 349.23, 440.00],
        [196.00, 261.63, 293.66, 349.23, 392.00]
      ]
    ];

    const currentProg = progressions[this.currentChordProgression % progressions.length];
    this.currentChordProgression++;

    let chordIndex = 0;
    const playNext = () => {
      if (!this.isPlaying || (this.currentMode !== 'lofi_synth' && !this.currentMode.startsWith('stream_'))) return;
      const notes = currentProg[chordIndex % currentProg.length];
      chordIndex++;
      this.playRhodesChord(notes, 4.0);
    };

    playNext();
    this.lofiTimer = setInterval(playNext, 4200);
  }

  playRhodesChord(freqs, duration) {
    if (!this.ctx) return;
    const now = this.ctx.currentTime;

    freqs.forEach((freq, idx) => {
      const osc1 = this.ctx.createOscillator();
      const osc2 = this.ctx.createOscillator();
      const noteGain = this.ctx.createGain();
      const filter = this.ctx.createBiquadFilter();

      // Warm vintage low-pass filter
      filter.type = 'lowpass';
      filter.frequency.setValueAtTime(850 + idx * 80, now);
      filter.frequency.exponentialRampToValueAtTime(320, now + duration);

      osc1.type = 'sine';
      osc2.type = 'triangle';

      const detune = (idx % 2 === 0 ? 1 : -1) * (2 + Math.random() * 3);
      osc1.frequency.setValueAtTime(freq, now);
      osc2.frequency.setValueAtTime(freq + detune, now);

      const stagger = idx * 0.045;
      const startTime = now + stagger;

      noteGain.gain.setValueAtTime(0.0001, startTime);
      noteGain.gain.linearRampToValueAtTime(0.07 / (1 + idx * 0.2), startTime + 0.08);
      noteGain.gain.exponentialRampToValueAtTime(0.0001, startTime + duration);

      osc1.connect(filter);
      osc2.connect(filter);
      filter.connect(noteGain);
      noteGain.connect(this.masterGain);

      osc1.start(startTime);
      osc2.start(startTime);
      osc1.stop(startTime + duration + 0.1);
      osc2.stop(startTime + duration + 0.1);
    });
  }

  // --- 3. RAIN SOUNDSCAPE ---
  startRain(isSolo = false) {
    if (!this.ctx) return;
    const bufferSize = this.ctx.sampleRate * 2;
    const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
    const data = buffer.getChannelData(0);

    for (let i = 0; i < bufferSize; i++) {
      data[i] = Math.random() * 2 - 1;
    }

    this.rainSource = this.ctx.createBufferSource();
    this.rainSource.buffer = buffer;
    this.rainSource.loop = true;

    const filter = this.ctx.createBiquadFilter();
    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(800, this.ctx.currentTime);

    this.rainGain = this.ctx.createGain();
    this.rainGain.gain.setValueAtTime(isSolo ? 0.35 : 0.15, this.ctx.currentTime);

    this.rainSource.connect(filter);
    filter.connect(this.rainGain);
    this.rainGain.connect(this.masterGain);

    this.rainSource.start();
  }

  // --- 4. ANALOG VINYL CRACKLE ---
  startVinyl() {
    if (!this.ctx) return;
    const bufferSize = this.ctx.sampleRate * 2;
    const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
    const data = buffer.getChannelData(0);

    for (let i = 0; i < bufferSize; i++) {
      const isPop = Math.random() < 0.0025;
      data[i] = isPop ? (Math.random() * 2 - 1) * 0.8 : (Math.random() * 2 - 1) * 0.015;
    }

    this.vinylSource = this.ctx.createBufferSource();
    this.vinylSource.buffer = buffer;
    this.vinylSource.loop = true;

    const filter = this.ctx.createBiquadFilter();
    filter.type = 'bandpass';
    filter.frequency.setValueAtTime(2500, this.ctx.currentTime);
    filter.Q.setValueAtTime(1.5, this.ctx.currentTime);

    this.vinylGain = this.ctx.createGain();
    this.vinylGain.gain.setValueAtTime(0.12, this.ctx.currentTime);

    this.vinylSource.connect(filter);
    filter.connect(this.vinylGain);
    this.vinylGain.connect(this.masterGain);

    this.vinylSource.start();
  }

  // --- 5. 40Hz GAMMA DEEP FOCUS BINAURAL BEATS ---
  startBinaural() {
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    
    this.binauralOscL = this.ctx.createOscillator();
    this.binauralOscR = this.ctx.createOscillator();
    this.binauralOscL.type = 'sine';
    this.binauralOscR.type = 'sine';
    this.binauralOscL.frequency.setValueAtTime(200, now);
    this.binauralOscR.frequency.setValueAtTime(240, now);

    const merger = this.ctx.createChannelMerger(2);
    this.binauralOscL.connect(merger, 0, 0);
    this.binauralOscR.connect(merger, 0, 1);

    this.binauralGain = this.ctx.createGain();
    this.binauralGain.gain.setValueAtTime(0.15, now);

    merger.connect(this.binauralGain);
    this.binauralGain.connect(this.masterGain);

    this.binauralOscL.start();
    this.binauralOscR.start();
  }

  // --- 6. BROWN NOISE (PURE FOCUS / ADHD CALMING) ---
  startBrownNoise() {
    if (!this.ctx) return;
    const bufferSize = this.ctx.sampleRate * 2;
    const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
    const data = buffer.getChannelData(0);

    let lastOut = 0.0;
    for (let i = 0; i < bufferSize; i++) {
      const white = Math.random() * 2 - 1;
      data[i] = (lastOut + (0.02 * white)) / 1.02;
      lastOut = data[i];
      data[i] *= 1.8;
    }

    this.brownSource = this.ctx.createBufferSource();
    this.brownSource.buffer = buffer;
    this.brownSource.loop = true;

    this.brownGain = this.ctx.createGain();
    this.brownGain.gain.setValueAtTime(0.3, this.ctx.currentTime);

    this.brownSource.connect(this.brownGain);
    this.brownGain.connect(this.masterGain);

    this.brownSource.start();
  }

  toggleVinyl() {
    this.vinylActive = !this.vinylActive;
    if (this.vinylActive && this.isPlaying) {
      this.startVinyl();
    } else if (!this.vinylActive && this.vinylSource) {
      try { this.vinylSource.stop(); } catch(e){}
      this.vinylSource = null;
    }
    return this.vinylActive;
  }

  toggleRain() {
    this.rainActive = !this.rainActive;
    if (this.rainActive && this.isPlaying) {
      this.startRain(false);
    } else if (!this.rainActive && this.rainSource && this.currentMode !== 'rain') {
      try { this.rainSource.stop(); } catch(e){}
      this.rainSource = null;
    }
    return this.rainActive;
  }

  playTimerBell() {
    this.initContext();
    const now = this.ctx.currentTime;
    const osc = this.ctx.createOscillator();
    const bellGain = this.ctx.createGain();

    osc.type = 'sine';
    osc.frequency.setValueAtTime(880, now);
    osc.frequency.exponentialRampToValueAtTime(440, now + 1.2);

    bellGain.gain.setValueAtTime(0.001, now);
    bellGain.gain.exponentialRampToValueAtTime(0.4, now + 0.05);
    bellGain.gain.exponentialRampToValueAtTime(0.0001, now + 2.5);

    osc.connect(bellGain);
    bellGain.connect(this.masterGain);

    osc.start(now);
    osc.stop(now + 2.6);
  }
}

// Global singleton instance
window.studyAudio = new StudyAudioManager();
