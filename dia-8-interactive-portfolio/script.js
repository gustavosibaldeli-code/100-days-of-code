// ==========================================
// SCRIPT UNIFICADO — AGENDA + PORTFÓLIO
// ==========================================

document.addEventListener("DOMContentLoaded", () => {

  // ==========================================
  // ELEMENTOS PRINCIPAIS
  // ==========================================

  const body = document.body;
  const html = document.documentElement;

  // ==========================================
  // DATA ATUAL
  // ==========================================

  const today = new Date();

  function formatDate(date) {
    return date.toLocaleDateString("pt-BR", {
      day: "2-digit",
      month: "2-digit",
      year: "numeric"
    });
  }

  function formatLongDate(date) {
    return date.toLocaleDateString("pt-BR", {
      weekday: "long",
      day: "numeric",
      month: "long",
      year: "numeric"
    });
  }

  const dateElements = document.querySelectorAll("#currentDate, .current-date, [data-current-date]");
  dateElements.forEach(el => {
    if (el.id === "currentDate") {
      el.textContent = formatLongDate(today);
    } else {
      el.textContent = formatLongDate(today);
    }
  });

  // ==========================================
  // SISTEMA DE CORES
  // ==========================================

  const colors = ["#6366f1", "#8b5cf6", "#ec4899", "#14b8a6", "#f59e0b", "#ef4444"];
  let currentColor = 0;

  const colorButton = document.querySelector("#colorButton");
  const primaryColorElement = document.documentElement;

  function changeColor() {
    currentColor = (currentColor + 1) % colors.length;
    const newColor = colors[currentColor];
    primaryColorElement.style.setProperty("--primary-color", newColor);
    primaryColorElement.style.setProperty("--accent-color", newColor);
    localStorage.setItem("agendaColor", newColor);
    showNotification("Cor da agenda alterada");
  }

  if (colorButton) {
    colorButton.addEventListener("click", changeColor);
  }

  const savedColor = localStorage.getItem("agendaColor");
  if (savedColor) {
    primaryColorElement.style.setProperty("--primary-color", savedColor);
    primaryColorElement.style.setProperty("--accent-color", savedColor);
    const savedIndex = colors.indexOf(savedColor);
    if (savedIndex !== -1) currentColor = savedIndex;
  }

  // ==========================================
  // MODO ESCURO / CLARO
  // ==========================================

  const themeButton = document.querySelector("#themeButton");
  const themeToggle = document.querySelector("#themeToggle");
  const themeIcon = document.querySelector("#themeIcon");

  function toggleTheme() {
    const isDark = html.getAttribute("data-theme") === "dark";
    const newTheme = isDark ? "light" : "dark";
    html.setAttribute("data-theme", newTheme);
    body.classList.toggle("dark-mode", newTheme === "dark");
    localStorage.setItem("agendaDarkMode", newTheme === "dark");
    themeIcon.textContent = newTheme === "dark" ? "🌙" : "☀️";
    showNotification(newTheme === "dark" ? "Modo escuro ativado" : "Modo claro ativado");
  }

  if (themeButton) {
    themeButton.addEventListener("click", toggleTheme);
  }

  if (themeToggle) {
    themeToggle.addEventListener("click", toggleTheme);
  }

  const savedTheme = localStorage.getItem("agendaDarkMode");
  if (savedTheme === "true" || savedTheme === null) {
    html.setAttribute("data-theme", "dark");
    body.classList.add("dark-mode");
    if (themeIcon) themeIcon.textContent = "🌙";
  } else if (savedTheme === "false") {
    html.setAttribute("data-theme", "light");
    body.classList.remove("dark-mode");
    if (themeIcon) themeIcon.textContent = "☀️";
  }

  // ==========================================
  // CALENDÁRIO
  // ==========================================

  function renderCalendar() {
    const calendar = document.getElementById("calendar");
    if (!calendar) return;

    const now = new Date();
    const year = now.getFullYear();
    const month = now.getMonth();

    const firstDay = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const todayDate = now.getDate();

    const dayNames = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"];
    let html = "";

    dayNames.forEach(name => {
      html += `<div class="day-name">${name}</div>`;
    });

    for (let i = 0; i < firstDay; i++) {
      html += `<div class="calendar-day empty"></div>`;
    }

    for (let d = 1; d <= daysInMonth; d++) {
      const isToday = d === todayDate ? "selected" : "";
      html += `<div class="calendar-day ${isToday}" data-day="${d}">${d}</div>`;
    }

    calendar.innerHTML = html;

    // Evento de seleção de dia
    document.querySelectorAll(".calendar-day:not(.empty)").forEach(day => {
      day.addEventListener("click", function() {
        document.querySelectorAll(".calendar-day").forEach(el => el.classList.remove("selected"));
        this.classList.add("selected");
        const selectedDate = this.dataset.day;
        showNotification(`Dia ${selectedDate} selecionado`);

        // Atualiza o campo de data do formulário
        const dateInput = document.querySelector("#appointmentForm input[name='date']");
        if (dateInput) {
          const year = now.getFullYear();
          const month = String(now.getMonth() + 1).padStart(2, '0');
          const day = String(selectedDate).padStart(2, '0');
          dateInput.value = `${year}-${month}-${day}`;
        }
      });
    });
  }

  renderCalendar();

  // ==========================================
  // COMPROMISSOS
  // ==========================================

  let appointments = JSON.parse(localStorage.getItem("agendaAppointments")) || [];

  const appointmentForm = document.querySelector("#appointmentForm");

  if (appointmentForm) {
    appointmentForm.addEventListener("submit", event => {
      event.preventDefault();

      const formData = new FormData(appointmentForm);
      const appointment = {
        id: Date.now(),
        title: formData.get("title") || "",
        date: formData.get("date") || formatDate(today),
        time: formData.get("time") || "",
        description: formData.get("description") || ""
      };

      if (!appointment.title) {
        showNotification("Digite um título para o compromisso");
        return;
      }

      appointments.push(appointment);
      localStorage.setItem("agendaAppointments", JSON.stringify(appointments));
      appointmentForm.reset();
      renderAppointments();
      showNotification("Compromisso adicionado");
    });
  }

  // ==========================================
  // EXIBIR COMPROMISSOS
  // ==========================================

  function escapeHTML(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
  }

  function renderAppointments() {
    const container = document.querySelector("#appointments");
    if (!container) return;

    container.innerHTML = "";

    if (appointments.length === 0) {
      container.innerHTML = `
        <div class="empty-appointments">
          Nenhum compromisso cadastrado.
        </div>
      `;
      return;
    }

    // Ordenar por data
    const sorted = [...appointments].sort((a, b) => {
      if (a.date < b.date) return -1;
      if (a.date > b.date) return 1;
      return 0;
    });

    sorted.forEach(appointment => {
      const item = document.createElement("div");
      item.className = "appointment-item";

      item.innerHTML = `
        <div class="appointment-info">
          <h4>${escapeHTML(appointment.title)}</h4>
          <div class="appointment-meta">
            ${escapeHTML(appointment.date)} ${appointment.time ? `· ${escapeHTML(appointment.time)}` : ''}
          </div>
          ${appointment.description ? `<div class="appointment-desc">${escapeHTML(appointment.description)}</div>` : ''}
        </div>
        <button class="btn-delete" data-id="${appointment.id}">Excluir</button>
      `;

      container.appendChild(item);
    });

    // Botões de excluir
    container.querySelectorAll(".btn-delete").forEach(button => {
      button.addEventListener("click", () => {
        const id = Number(button.dataset.id);
        appointments = appointments.filter(a => a.id !== id);
        localStorage.setItem("agendaAppointments", JSON.stringify(appointments));
        renderAppointments();
        showNotification("Compromisso excluído");
      });
    });
  }

  renderAppointments();

  // ==========================================
  // NOTIFICAÇÕES
  // ==========================================

  function showNotification(message) {
    const oldNotification = document.querySelector(".agenda-notification");
    if (oldNotification) oldNotification.remove();

    const notification = document.createElement("div");
    notification.className = "agenda-notification";
    notification.textContent = message;
    document.body.appendChild(notification);

    requestAnimationFrame(() => {
      notification.classList.add("show");
    });

    setTimeout(() => {
      notification.classList.remove("show");
      setTimeout(() => notification.remove(), 300);
    }, 2500);
  }

  // ==========================================
  // SCROLL PROGRESS
  // ==========================================

  const progressBar = document.getElementById("scrollProgressBar");

  function updateScrollProgress() {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    if (progressBar) {
      progressBar.style.width = `${progress}%`;
    }
  }

  window.addEventListener("scroll", updateScrollProgress);
  window.addEventListener("resize", updateScrollProgress);
  updateScrollProgress();

  // ==========================================
  // REVEAL ANIMATIONS (Intersection Observer)
  // ==========================================

  const revealElements = document.querySelectorAll(".reveal");

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: "0px 0px -40px 0px"
  });

  revealElements.forEach(el => observer.observe(el));

  // ==========================================
  // SKILLS BAR ANIMATION
  // ==========================================

  const skillCards = document.querySelectorAll(".skill-card");

  const skillObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const fill = entry.target.querySelector(".skill-bar-fill");
        const percent = entry.target.dataset.percent || 0;
        if (fill) {
          fill.style.width = `${percent}%`;
        }
      }
    });
  }, { threshold: 0.2 });

  skillCards.forEach(card => skillObserver.observe(card));

  // ==========================================
  // COUNTER ANIMATION
  // ==========================================

  const counters = document.querySelectorAll(".counter");

  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const target = parseInt(entry.target.dataset.target) || 0;
        animateCounter(entry.target, target);
        counterObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });

  counters.forEach(counter => counterObserver.observe(counter));

  function animateCounter(element, target) {
    let current = 0;
    const increment = Math.max(1, Math.floor(target / 60));
    const duration = 2000;
    const startTime = performance.now();

    function updateCounter(time) {
      const elapsed = time - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      current = Math.floor(eased * target);
      element.textContent = current;

      if (progress < 1) {
        requestAnimationFrame(updateCounter);
      } else {
        element.textContent = target;
      }
    }

    requestAnimationFrame(updateCounter);
  }

  // ==========================================
  // CURSOR PERSONALIZADO
  // ==========================================

  const cursorDot = document.querySelector(".cursor-dot");
  const cursorRing = document.querySelector(".cursor-ring");

  if (cursorDot && cursorRing) {
    let mouseX = 0, mouseY = 0;
    let ringX = 0, ringY = 0;

    document.addEventListener("mousemove", (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;

      cursorDot.style.left = `${mouseX}px`;
      cursorDot.style.top = `${mouseY}px`;

      // Smooth ring follow
      ringX += (mouseX - ringX) * 0.12;
      ringY += (mouseY - ringY) * 0.12;

      cursorRing.style.left = `${ringX}px`;
      cursorRing.style.top = `${ringY}px`;

      // Spray light
      document.documentElement.style.setProperty("--mx", `${(mouseX / window.innerWidth) * 100}%`);
      document.documentElement.style.setProperty("--my", `${(mouseY / window.innerHeight) * 100}%`);
    });

    document.querySelectorAll("a, button, .calendar-day, .skill-card, .tilt-card, .appointment-item").forEach(el => {
      el.addEventListener("mouseenter", () => cursorRing.classList.add("is-hover"));
      el.addEventListener("mouseleave", () => cursorRing.classList.remove("is-hover"));
    });
  }

  // ==========================================
  // TILT CARD 3D
  // ==========================================

  const tiltCard = document.querySelector("#tiltCard");

  if (tiltCard) {
    const glow = tiltCard.querySelector(".tilt-card-glow");

    tiltCard.addEventListener("mousemove", (e) => {
      const rect = tiltCard.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      const rotateX = ((y - centerY) / centerY) * -8;
      const rotateY = ((x - centerX) / centerX) * 8;

      tiltCard.style.transform =
        `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.02)`;

      if (glow) {
        const gx = (x / rect.width) * 100;
        const gy = (y / rect.height) * 100;
        glow.style.setProperty("--gx", `${gx}%`);
        glow.style.setProperty("--gy", `${gy}%`);
      }
    });

    tiltCard.addEventListener("mouseleave", () => {
      tiltCard.style.transform = "rotateX(0deg) rotateY(0deg) scale(1)";
    });
  }

  // ==========================================
  // PARALLAX FLOATING TAGS
  // ==========================================

  document.querySelectorAll("[data-depth]").forEach(el => {
    const depth = parseFloat(el.dataset.depth) || 0.05;
    const speed = depth * 20;

    document.addEventListener("mousemove", (e) => {
      const x = (e.clientX / window.innerWidth - 0.5) * speed;
      const y = (e.clientY / window.innerHeight - 0.5) * speed;
      el.style.transform = `translate(${x}px, ${y}px)`;
    });
  });

  // ==========================================
  // CONSOLE
  // ==========================================

  console.log("✓ Gustavo Dev Experience carregada com sucesso!");
  console.log("✓ Agenda Interativa integrada ao portfolio!");

  // Expor showNotification globalmente para uso em outros contextos
  window.showNotification = showNotification;

});