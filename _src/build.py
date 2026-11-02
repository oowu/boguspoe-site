"""Собирает языковые версии сайта из _src/template.html.

Запуск из корня репозитория:  python3 _src/build.py
Создаёт: index.html (RU), pl/index.html, en/index.html
"""
import html
import os
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://boguspoe.dev"

LANGS = [
    # код, путь, подпись в переключателе, og:locale
    ("ru", "/", "RU", "ru_RU"),
    ("pl", "/pl/", "PL", "pl_PL"),
    ("en", "/en/", "EN", "en_US"),
]

T = {
    "ru": {
        "title": "boguspoe.dev — сайты, Telegram-боты и ИИ-автоматизация",
        "description": "bogdan, вайб-кодер из Варшавы. Сайты любого типа, Telegram-боты, n8n-автоматизация и внедрение ИИ-агентов в проекты.",
        "og_desc": "Вайб-кодер bogdan: сайты, Telegram-боты, n8n и ИИ-агенты под задачи бизнеса.",
        "secret": "СЕКРЕТ НАЙДЕН! +1 ЖИЗНЬ",
        "nav_label": "Основное меню",
        "lang_label": "Язык",
        "nav_about": "ОБО МНЕ", "nav_skills": "НАВЫКИ", "nav_projects": "ПРОЕКТЫ", "nav_contact": "КОНТАКТЫ",
        "hello": "ИГРОК 1 ПОДКЛЮЧИЛСЯ",
        "hi": "ПРИВЕТ! Я",
        "intro": "Вайб-кодер. Собираю все виды сайтов и Telegram-ботов при помощи своих знаний и ИИ — быстро, понятно, под задачи живого бизнеса и клиента.",
        "btn_start": "НАЧАТЬ ИГРУ", "btn_levels": "УРОВНИ",
        "avatar_label": "Пиксельный аватар bogdan",
        "st_nick": "НИК", "st_class": "КЛАСС", "v_class": "ВАЙБ-КОДЕР",
        "st_loc": "ЛОКАЦИЯ", "v_loc": "ВАРШАВА",
        "st_status": "СТАТУС", "v_status": "ОТКРЫТ К ЗАКАЗАМ",
        "st_charge": "ЗАРЯД ИДЕЙ",
        "h_inventory": "ИНВЕНТАРЬ",
        "inv_lead": "Инструменты, которыми я собираю проекты от идеи до запуска.",
        "sk_html": "Вёрстка сайтов любого типа",
        "sk_py": "Боты, скрипты, бэкенд",
        "sk_tg": "Боты под любые бизнес-задачи",
        "sk_gh": "Код и версии проекта",
        "sk_host_n": "ХОСТИНГИ И АВТОДЕПЛОЙ", "sk_host": "Любые хостинги, обновления в один клик",
        "sk_ai_n": "ИИ-КОДИНГ",
        "sk_n8n_n": "N8N И АВТОМАТИЗАЦИЯ", "sk_n8n": "Связываю сервисы и убираю рутину",
        "sk_ag_n": "ИИ-АГЕНТЫ", "sk_ag": "Внедрение агентов в проекты",
        "h_levels": "ПРОЙДЕННЫЕ УРОВНИ",
        "p1_alt": "Главный экран сайта Ocean Beauty",
        "p1_lvl": "УРОВЕНЬ 1 · ПРОЙДЕН",
        "p1_desc": "Сайт-визитка салона красоты в Варшаве: четыре языка, адаптация под телефон, автодеплой из GitHub на Netlify.",
        "p1_go": "ОТКРЫТЬ САЙТ",
        "p2_alt": "Профиль Telegram-бота OceanBeautyCourseBot",
        "p2_lvl": "УРОВЕНЬ 2 · ПРОЙДЕН",
        "p2_title": "БОТ ЗАПИСИ НА КУРСЫ",
        "p2_desc": "Telegram-бот на Python для записи на курсы маникюра и педикюра. Работает на удалённом сервере.",
        "tag_server": "Сервер",
        "p2_go": "ОТКРЫТЬ БОТА",
        "p3_lvl": "УРОВЕНЬ 3", "p3_locked": "ЗАБЛОКИРОВАН",
        "p3_desc": "Здесь может быть ваш проект.",
        "p3_go": "РАЗБЛОКИРОВАТЬ",
        "h_quest": "КАК ПРОХОДИМ КВЕСТ",
        "s1": "БРИФ", "s1d": "Обсуждаем задачу, цели и сроки.",
        "s2": "ПРОТОТИП", "s2d": "Собираю первую версию, которую можно потрогать.",
        "s3": "ПРАВКИ", "s3d": "Доводим до результата вместе.",
        "s4": "ЗАПУСК", "s4d": "Публикую и показываю, как обновлять.",
        "contact": "Нужен сайт, Telegram-бот или автоматизация с ИИ? Напишите — обсудим задачу.",
    },
    "pl": {
        "title": "boguspoe.dev — strony, boty Telegram i automatyzacja AI",
        "description": "bogdan, vibe-coder z Warszawy. Strony internetowe każdego typu, boty Telegram, automatyzacja n8n i wdrażanie agentów AI.",
        "og_desc": "Vibe-coder bogdan: strony, boty Telegram, n8n i agenci AI dopasowani do potrzeb biznesu.",
        "secret": "SEKRET ODNALEZIONY! +1 ŻYCIE",
        "nav_label": "Menu główne",
        "lang_label": "Język",
        "nav_about": "O MNIE", "nav_skills": "UMIEJĘTNOŚCI", "nav_projects": "PROJEKTY", "nav_contact": "KONTAKT",
        "hello": "GRACZ 1 DOŁĄCZYŁ",
        "hi": "CZEŚĆ! JESTEM",
        "intro": "Vibe-coder. Tworzę strony internetowe każdego rodzaju i boty Telegram, łącząc własną wiedzę z AI — szybko, zrozumiale i pod realne potrzeby biznesu i klienta.",
        "btn_start": "START GRY", "btn_levels": "POZIOMY",
        "avatar_label": "Pikselowy awatar bogdana",
        "st_nick": "NICK", "st_class": "KLASA", "v_class": "VIBE-CODER",
        "st_loc": "LOKACJA", "v_loc": "WARSZAWA",
        "st_status": "STATUS", "v_status": "PRZYJMUJĘ ZLECENIA",
        "st_charge": "ENERGIA POMYSŁÓW",
        "h_inventory": "EKWIPUNEK",
        "inv_lead": "Narzędzia, z których buduję projekty od pomysłu do startu.",
        "sk_html": "Strony internetowe każdego typu",
        "sk_py": "Boty, skrypty, backend",
        "sk_tg": "Boty do każdego zadania biznesowego",
        "sk_gh": "Kod i wersje projektu",
        "sk_host_n": "HOSTING I AUTODEPLOY", "sk_host": "Dowolny hosting, aktualizacje jednym kliknięciem",
        "sk_ai_n": "KODOWANIE Z AI",
        "sk_n8n_n": "N8N I AUTOMATYZACJA", "sk_n8n": "Łączę serwisy i usuwam rutynę",
        "sk_ag_n": "AGENCI AI", "sk_ag": "Wdrażanie agentów w projektach",
        "h_levels": "UKOŃCZONE POZIOMY",
        "p1_alt": "Ekran główny strony Ocean Beauty",
        "p1_lvl": "POZIOM 1 · UKOŃCZONY",
        "p1_desc": "Strona-wizytówka salonu kosmetycznego w Warszawie: cztery języki, wersja mobilna, automatyczny deploy z GitHuba na Netlify.",
        "p1_go": "OTWÓRZ STRONĘ",
        "p2_alt": "Profil bota Telegram OceanBeautyCourseBot",
        "p2_lvl": "POZIOM 2 · UKOŃCZONY",
        "p2_title": "BOT DO ZAPISÓW NA KURSY",
        "p2_desc": "Bot Telegram w Pythonie do zapisów na kursy manicure i pedicure. Działa na zdalnym serwerze.",
        "tag_server": "Serwer",
        "p2_go": "OTWÓRZ BOTA",
        "p3_lvl": "POZIOM 3", "p3_locked": "ZABLOKOWANY",
        "p3_desc": "Tu może być Twój projekt.",
        "p3_go": "ODBLOKUJ",
        "h_quest": "JAK PRZECHODZIMY QUEST",
        "s1": "BRIEF", "s1d": "Omawiamy zadanie, cele i terminy.",
        "s2": "PROTOTYP", "s2d": "Buduję pierwszą wersję, którą można przetestować.",
        "s3": "POPRAWKI", "s3d": "Razem dopracowujemy wynik.",
        "s4": "START", "s4d": "Publikuję i pokazuję, jak aktualizować.",
        "contact": "Potrzebujesz strony, bota Telegram lub automatyzacji z AI? Napisz — omówimy zadanie.",
    },
    "en": {
        "title": "boguspoe.dev — websites, Telegram bots & AI automation",
        "description": "bogdan, a vibe-coder in Warsaw. Websites of any kind, Telegram bots, n8n automation and AI agent integration.",
        "og_desc": "Vibe-coder bogdan: websites, Telegram bots, n8n and AI agents built around real business needs.",
        "secret": "SECRET FOUND! +1 UP",
        "nav_label": "Main menu",
        "lang_label": "Language",
        "nav_about": "ABOUT", "nav_skills": "SKILLS", "nav_projects": "PROJECTS", "nav_contact": "CONTACT",
        "hello": "PLAYER 1 HAS JOINED",
        "hi": "HI! I'M",
        "intro": "Vibe-coder. I build all kinds of websites and Telegram bots, combining my own know-how with AI — fast, clear and shaped around real business and client needs.",
        "btn_start": "START GAME", "btn_levels": "LEVELS",
        "avatar_label": "Pixel avatar of bogdan",
        "st_nick": "NICK", "st_class": "CLASS", "v_class": "VIBE-CODER",
        "st_loc": "LOCATION", "v_loc": "WARSAW",
        "st_status": "STATUS", "v_status": "OPEN FOR WORK",
        "st_charge": "IDEA ENERGY",
        "h_inventory": "INVENTORY",
        "inv_lead": "The tools I use to take projects from idea to launch.",
        "sk_html": "Websites of any kind",
        "sk_py": "Bots, scripts, backend",
        "sk_tg": "Bots for any business task",
        "sk_gh": "Code and version control",
        "sk_host_n": "HOSTING & AUTO-DEPLOY", "sk_host": "Any hosting, one-click updates",
        "sk_ai_n": "AI CODING",
        "sk_n8n_n": "N8N & AUTOMATION", "sk_n8n": "Connecting services, removing routine work",
        "sk_ag_n": "AI AGENTS", "sk_ag": "Integrating agents into projects",
        "h_levels": "COMPLETED LEVELS",
        "p1_alt": "Home screen of the Ocean Beauty website",
        "p1_lvl": "LEVEL 1 · CLEARED",
        "p1_desc": "Business-card website for a beauty salon in Warsaw: four languages, mobile-first, auto-deploy from GitHub to Netlify.",
        "p1_go": "OPEN SITE",
        "p2_alt": "Profile of the OceanBeautyCourseBot Telegram bot",
        "p2_lvl": "LEVEL 2 · CLEARED",
        "p2_title": "COURSE SIGN-UP BOT",
        "p2_desc": "Python Telegram bot for manicure and pedicure course sign-ups. Runs on a remote server.",
        "tag_server": "Server",
        "p2_go": "OPEN BOT",
        "p3_lvl": "LEVEL 3", "p3_locked": "LOCKED",
        "p3_desc": "Your project could be here.",
        "p3_go": "UNLOCK",
        "h_quest": "HOW THE QUEST GOES",
        "s1": "BRIEF", "s1d": "We discuss the task, goals and timeline.",
        "s2": "PROTOTYPE", "s2d": "I build a first version you can try out.",
        "s3": "REVISIONS", "s3d": "We polish it together.",
        "s4": "LAUNCH", "s4d": "I publish it and show you how to update it.",
        "contact": "Need a website, a Telegram bot or AI automation? Message me — let's talk it through.",
    },
}


def build():
    tpl = open(os.path.join(ROOT, "_src", "template.html"), encoding="utf-8").read()
    ver = time.strftime("%Y%m%d%H%M")
    hreflang = "\n".join(
        f'<link rel="alternate" hreflang="{c}" href="{SITE}{p}">' for c, p, _, _ in LANGS
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{SITE}/">'

    for code, path, label, locale in LANGS:
        t = dict(T[code])
        missing = set(T["ru"]) ^ set(t)
        assert not missing, f"{code}: не хватает ключей {missing}"
        langs = "".join(
            f'<a href="{p}" hreflang="{c}" lang="{c}"'
            + (' aria-current="true"' if c == code else "")
            + f">{l}</a>"
            for c, p, l, _ in LANGS
        )
        out = tpl
        values = {k: html.escape(v, quote=True) for k, v in t.items()}
        values.update(lang=code, url=SITE + path, og_locale=locale,
                      hreflang=hreflang, langs=langs, ver=ver)
        for k, v in values.items():
            out = out.replace("{{" + k + "}}", v)
        assert "{{" not in out, f"{code}: остались незаполненные места"
        dest = os.path.join(ROOT, path.strip("/"), "index.html")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(out)
        print("собрано:", os.path.relpath(dest, ROOT))


if __name__ == "__main__":
    build()
