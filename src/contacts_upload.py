import asyncio

from sqlalchemy import select

from .bot.core.db import AsyncSessionLocal
from .bot.models import (
    Contact,
    ContactKeyword,
    Department,
    DepartmentJobTitle,
    JobTitle,
    Keyword,
    Position,
)
from .bot.utils.keyword_search import prepare_words


CONTACTS_RAW = [
    [
        'Абасова Лариса Кязим кызы',
        '+79161591412',
        '',
        'l.abasova@vtoroe.ru',
    ],
    ['Авакян Ева', '', '@vlasova_eva', 'smm@vtoroe.ru'],
    [
        'Аверин Дмитрий Викторович',
        '',
        '@d_averin',
        'd.averin@vtoroe.ru',
    ],
    [
        'Алексеева Дарья Владимировна',
        '',
        '@alekseevadaria',
        'da@vtoroe.ru',
    ],
    [
        'Бабайцева Юлия Олеговна',
        '',
        '@byo17',
        'y.babaytseva@vtoroe.ru',
    ],
    [
        'Блинова Дарья Александровна',
        '',
        '@danyakosha',
        'd.blinova@vtoroe.ru',
    ],
    [
        'Васинская Яна Владимировна',
        '+79607452424',
        '',
        'kostroma.centr@vtoroe.ru',
    ],
    [
        'Герасимова Инна Сергеевна',
        '+79032948194',
        '',
        'inna@vtoroe.ru',
    ],
    [
        'Герасимовская Алина Алексеевна',
        '',
        '@alyamovskaya19',
        'a.gerasimovskaya@vtoroe.ru',
    ],
    [
        'Голикова Вероника Владимировна',
        '',
        '@golikovanika',
        'v.golikova@vtoroe.ru',
    ],
    [
        'Гринягин Андрей Юрьевич',
        '+79621886702',
        '',
        'a.grinyagin@vtoroe.ru',
    ],
    [
        'Двоеглазова Дарина Вячеславовна',
        '',
        '@ImDarinaD',
        'd.dvoeglazova@vtoroe.ru',
    ],
    [
        'Дудченко Ангелина Александровна',
        '',
        '@ewgtfo',
        'a.dudchenko@vtoroe.ru',
    ],
    [
        'Золотухина Юлия Юрьевна',
        '',
        '@yzolotuhina',
        'y.zolotuhina@vtoroe.ru',
    ],
    [
        'Иванов (Жданов) Даниил Иванович',
        '',
        '@DanZhdanov',
        'd.zhdanov@vtoroe.ru',
    ],
    [
        'Каримова Анастасия Алексеевна',
        '',
        '@anastaskarim',
        'a.karimova@vtoroe.ru',
    ],
    [
        'Кнутова Елена Геннадьевна',
        '+79502439206',
        '',
        'e.knutova@vtoroe.ru',
    ],
    [
        'Козловских Ирина Анатольевна',
        '',
        '@irinakozlovskikh',
        'i.kozlovskikh@vtoroe.ru',
    ],
    [
        'Кудряшова Наталья Андреевна',
        '',
        '@natkudryashova',
        'hr@vtoroe.ru',
    ],
    [
        'Малярова Светлана Александровна',
        '+79035488829',
        '',
        's.malyarova@vtoroe.ru',
    ],
    [
        'Матвеева Наталья Владимировна',
        '',
        '@matveeva_n_v',
        'n.matveeva@vtoroe.ru',
    ],
    ['Матюхина Юлия Андреевна', '', '@mayulya', 'ym@vtoroe.ru'],
    [
        'Молчанов Иван Александрович',
        '',
        '@Mol4anof',
        'i.molchanov@vtoroe.ru',
    ],
    [
        'Морозова Вера Юрьевна',
        '',
        '@kulemushka',
        'v.morozova@vtoroe.ru',
    ],
    [
        'Наседкина Алина Геннадьевна',
        '',
        '@alinanasedkina',
        'a.nasedkina@vtoroe.ru',
    ],
    [
        'Обновленская Юлия Сергеевна',
        '',
        '@obnovlenskaya',
        'y.obnovlenskaya@vtoroe.ru',
    ],
    [
        'Песоцкая Татьяна Юрьевна',
        '',
        '@tpesotskaya',
        't.pesotskaya@vtoroe.ru',
    ],
    [
        'Сапрыгина Мария Юрьевна',
        '',
        '@Maria_Maria1234567',
        'buh@vtoroe.ru',
    ],
    [
        'Свиридов Сергей Андреевич',
        '',
        '@sergei_sviridoff',
        's.sviridov@vtoroe.ru',
    ],
    [
        'Селезнева Юлия Валерьевна',
        '',
        '@JuliSelezneva',
        'us@vtoroe.ru',
    ],
    ['Сиваева Екатерина Олеговна', '', '', 'e.sivaeva@vtoroe.ru'],
    [
        'Скопенко Оксана Евгеньевна',
        '+79060946799',
        '',
        'o.skopenko@vtoroe.ru',
    ],
    [
        'Соркина Наталья Викторовна',
        '',
        '@Natanelllll',
        'n.sorkina@vtoroe.ru',
    ],
    [
        'Теплинская Наталья Викторовна',
        '',
        '@Natali_Teplinskaya',
        'n.teplinskaya@vtoroe.ru',
    ],
    [
        'Ткаченко Алексей Владимирович',
        '',
        '@Atchko',
        'a.tkachenko@vtoroe.ru',
    ],
    [
        'Трунина Елена Сергеевна',
        '',
        '@trunyaelena',
        'e.trunina@vtoroe.ru',
    ],
    [
        'Тюрин Андрей Александрович',
        '+79607492618',
        '',
        'sklad.kostroma@vtoroe.ru',
    ],
    ['Тюрина Ирина Александровна', '', '', 'i.tiurina@vtoroe.ru'],
    [
        'Уварова Ксения Анатольевна',
        '',
        '@KsenyaUvarova',
        'k.uvarova@vtoroe.ru',
    ],
    [
        'Цветкова Анастасия Станиславовна',
        '',
        '@atsvett',
        'a.tsvetkova@vtoroe.ru',
    ],
    ['Цой Дмитрий Витальевич', '+79687367713', '', 'd.tsoy@vtoroe.ru'],
    ['Цой Лариса Владимировна', '', '@LaraTsoi', 'l.tsoy@vtoroe.ru'],
    [
        'Чугринова Евгения Александровна',
        '',
        '@jenyajenechka',
        'e.chugrinova@vtoroe.ru',
    ],
]

DEPARTMENTS_RAW = [
    'Финансово-административный отдел',
    'Мастерская г. Москва',
    'Отдел по работе с партнерами',
    'Дирекция',
    'Руководители и специалисты в прямом подчинении Директору',
    'Отдел информационных программ',
    'Центр гуманитарной выдачи г. Кострома',
    'Отдел коммуникаций',
    'Центр сортировки и переработки г. Кострома',
    'Отдел благотворительных программ',
    'Центр сортировки г. Москва',
    'Руководители и специалисты в прямом подчинении Программному директору',
    'Отдел управления персоналом',
    'Административный отдел',
    'Специалисты и подразделения в прямом подчинении Финансовому директору',
]

JOB_TITLES_RAW = [
    'Юрисконсульт',
    'Администратор мастерской',
    'Координатор отдела по работе с В2В партнерами',
    'Директор',
    'Бизнес-ассистент',
    'Менеджер проектов',
    'Администратор центра выдачи',
    'Координатор по работе с партнерами',
    'Контент-продюсер',
    'Директор склада г. Кострома',
    'Координатор благотворительных программ',
    'Менеджер информационных программ',
    'Event-менеджер',
    'Медиакоординатор',
    'Ассистент отдела по работе с партнерами',
    'Координатор центра выдачи',
    'PR-директор',
    'HR-директор',
    'Директор по складской и транспортной логистике',
    'Руководитель мастерской г. Москва',
    'Финансовый директор',
    'Координатор региональных благотворительных программ',
    'Руководитель отдела информационных программ',
    'Фандрайзер',
    'Менеджер программ по обмену опытом',
    'Программный директор',
    'Бухгалтер',
    'Младший фандрайзер',
    'Ведущий координатор благотворительных программ',
    'Младший менеджер по логистике',
    'Бухгалтер по заработной плате',
    'Главный бухгалтер',
    'Руководитель отдела благотворительных программ',
    'Директор по сбору и рециклингу текстиля',
    'HR-менеджер',
    'Кладовщик',
    'Менеджер по обучению и развитию персонала',
    'Email-маркетолог',
    'Финансовый менеджер',
    'Администратор',
    'Заместитель директора по складской и транспортной логистике',
    'Руководитель административного отдела',
    'Руководитель отдела по работе с партнерами',
]


DEPARTMENT_JOB_TITLE_RAW = [
    ['Юрисконсульт', 'Финансово-административный отдел'],
    ['Администратор мастерской', 'Мастерская г. Москва'],
    [
        'Координатор отдела по работе с В2В партнерами',
        'Отдел по работе с партнерами',
    ],
    ['Директор', 'Дирекция'],
    [
        'Бизнес-ассистент',
        'Руководители и специалисты в прямом подчинении Директору',
    ],
    ['Менеджер проектов', 'Отдел информационных программ'],
    [
        'Администратор центра выдачи',
        'Центр гуманитарной выдачи г. Кострома',
    ],
    [
        'Координатор по работе с партнерами',
        'Отдел по работе с партнерами',
    ],
    ['Контент-продюсер', 'Отдел коммуникаций'],
    [
        'Директор склада г. Кострома',
        'Центр сортировки и переработки г. Кострома',
    ],
    [
        'Координатор благотворительных программ',
        'Отдел благотворительных программ',
    ],
    [
        'Менеджер информационных программ',
        'Отдел информационных программ',
    ],
    ['Event-менеджер', 'Отдел коммуникаций'],
    ['Медиакоординатор', 'Отдел коммуникаций'],
    [
        'Ассистент отдела по работе с партнерами',
        'Отдел по работе с партнерами',
    ],
    [
        'Координатор центра выдачи',
        'Центр гуманитарной выдачи г. Кострома',
    ],
    [
        'PR-директор',
        'Руководители и специалисты в прямом подчинении Директору',
    ],
    [
        'HR-директор',
        'Руководители и специалисты в прямом подчинении Директору',
    ],
    [
        'Директор по складской и транспортной логистике',
        'Центр сортировки г. Москва',
    ],
    [
        'Руководитель мастерской г. Москва',
        'Руководители и специалисты в прямом подчинении Программному директору',  # noqa
    ],
    [
        'Финансовый директор',
        'Руководители и специалисты в прямом подчинении Директору',
    ],
    [
        'Координатор региональных благотворительных программ',
        'Отдел благотворительных программ',
    ],
    [
        'Руководитель отдела информационных программ',
        'Руководители и специалисты в прямом подчинении Программному директору',  # noqa
    ],
    ['Фандрайзер', 'Отдел коммуникаций'],
    [
        'Менеджер программ по обмену опытом',
        'Отдел информационных программ',
    ],
    [
        'Программный директор',
        'Руководители и специалисты в прямом подчинении Директору',
    ],
    ['Бухгалтер', 'Финансово-административный отдел'],
    ['Младший фандрайзер', 'Отдел коммуникаций'],
    [
        'Ведущий координатор благотворительных программ',
        'Отдел благотворительных программ',
    ],
    ['Младший менеджер по логистике', 'Центр сортировки г. Москва'],
    [
        'Бухгалтер по заработной плате',
        'Финансово-административный отдел',
    ],
    ['Бухгалтер по заработной плате', 'Отдел управления персоналом'],
    ['Главный бухгалтер', 'Финансово-административный отдел'],
    [
        'Руководитель отдела благотворительных программ',
        'Руководители и специалисты в прямом подчинении Программному директору',  # noqa
    ],
    [
        'Директор по сбору и рециклингу текстиля',
        'Руководители и специалисты в прямом подчинении Директору',
    ],
    ['HR-менеджер', 'Отдел управления персоналом'],
    ['Кладовщик', 'Центр сортировки и переработки г. Кострома'],
    [
        'Менеджер по обучению и развитию персонала',
        'Отдел управления персоналом',
    ],
    ['Email-маркетолог', 'Отдел коммуникаций'],
    ['Финансовый менеджер', 'Финансово-административный отдел'],
    ['Администратор', 'Административный отдел'],
    [
        'Заместитель директора по складской и транспортной логистике',
        'Центр сортировки г. Москва',
    ],
    [
        'Руководитель административного отдела',
        'Специалисты и подразделения в прямом подчинении Финансовому директору',  # noqa
    ],
    [
        'Руководитель отдела по работе с партнерами',
        'Отдел по работе с партнерами',
    ],
]

POSITION_RAW = [
    [
        'Абасова Лариса Кязим кызы',
        'Юрисконсульт',
        'Финансово-административный отдел',
    ],
    ['Авакян Ева', 'Администратор мастерской', 'Мастерская г. Москва'],
    [
        'Аверин Дмитрий Викторович',
        'Координатор отдела по работе с В2В партнерами',
        'Отдел по работе с партнерами',
    ],
    ['Алексеева Дарья Владимировна', 'Директор', 'Дирекция'],
    [
        'Бабайцева Юлия Олеговна',
        'Бизнес-ассистент',
        'Руководители и специалисты в прямом подчинении Директору',
    ],
    [
        'Блинова Дарья Александровна',
        'Менеджер проектов',
        'Отдел информационных программ',
    ],
    [
        'Васинская Яна Владимировна',
        'Администратор центра выдачи',
        'Центр гуманитарной выдачи г. Кострома',
    ],
    [
        'Герасимова Инна Сергеевна',
        'Координатор по работе с партнерами',
        'Отдел по работе с партнерами',
    ],
    [
        'Герасимовская Алина Алексеевна',
        'Координатор по работе с партнерами',
        'Отдел по работе с партнерами',
    ],
    [
        'Голикова Вероника Владимировна',
        'Контент-продюсер',
        'Отдел коммуникаций',
    ],
    [
        'Гринягин Андрей Юрьевич',
        'Директор склада г. Кострома',
        'Центр сортировки и переработки г. Кострома',
    ],
    [
        'Двоеглазова Дарина Вячеславовна',
        'Координатор благотворительных программ',
        'Отдел благотворительных программ',
    ],
    [
        'Дудченко Ангелина Александровна',
        'Менеджер информационных программ',
        'Отдел информационных программ',
    ],
    [
        'Золотухина Юлия Юрьевна',
        'Event-менеджер',
        'Отдел коммуникаций',
    ],
    [
        'Иванов (Жданов) Даниил Иванович',
        'Медиакоординатор',
        'Отдел коммуникаций',
    ],
    [
        'Каримова Анастасия Алексеевна',
        'Ассистент отдела по работе с партнерами',
        'Отдел по работе с партнерами',
    ],
    [
        'Кнутова Елена Геннадьевна',
        'Координатор центра выдачи',
        'Центр гуманитарной выдачи г. Кострома',
    ],
    [
        'Козловских Ирина Анатольевна',
        'PR-директор',
        'Руководители и специалисты в прямом подчинении Директору',
    ],
    [
        'Кудряшова Наталья Андреевна',
        'HR-директор',
        'Руководители и специалисты в прямом подчинении Директору',
    ],
    [
        'Малярова Светлана Александровна',
        'Директор по складской и транспортной логистике',
        'Центр сортировки г. Москва',
    ],
    [
        'Матвеева Наталья Владимировна',
        'Руководитель мастерской г. Москва',
        'Руководители и специалисты в прямом подчинении Программному директору',  # noqa
    ],
    [
        'Матюхина Юлия Андреевна',
        'Финансовый директор',
        'Руководители и специалисты в прямом подчинении Директору',
    ],
    [
        'Молчанов Иван Александрович',
        'Координатор региональных благотворительных программ',
        'Отдел благотворительных программ',
    ],
    [
        'Морозова Вера Юрьевна',
        'Руководитель отдела информационных программ',
        'Руководители и специалисты в прямом подчинении Программному директору',  # noqa
    ],
    [
        'Наседкина Алина Геннадьевна',
        'Фандрайзер',
        'Отдел коммуникаций',
    ],
    [
        'Обновленская Юлия Сергеевна',
        'Менеджер программ по обмену опытом',
        'Отдел информационных программ',
    ],
    [
        'Песоцкая Татьяна Юрьевна',
        'Программный директор',
        'Руководители и специалисты в прямом подчинении Директору',
    ],
    [
        'Сапрыгина Мария Юрьевна',
        'Бухгалтер',
        'Финансово-административный отдел',
    ],
    [
        'Свиридов Сергей Андреевич',
        'Младший фандрайзер',
        'Отдел коммуникаций',
    ],
    [
        'Селезнева Юлия Валерьевна',
        'Ведущий координатор благотворительных программ',
        'Отдел благотворительных программ',
    ],
    [
        'Сиваева Екатерина Олеговна',
        'Младший менеджер по логистике',
        'Центр сортировки г. Москва',
    ],
    [
        'Скопенко Оксана Евгеньевна',
        'Бухгалтер по заработной плате',
        'Финансово-административный отдел',
    ],
    [
        'Скопенко Оксана Евгеньевна',
        'Бухгалтер по заработной плате',
        'Отдел управления персоналом',
    ],
    [
        'Соркина Наталья Викторовна',
        'Главный бухгалтер',
        'Финансово-административный отдел',
    ],
    [
        'Теплинская Наталья Викторовна',
        'Руководитель отдела благотворительных программ',
        'Руководители и специалисты в прямом подчинении Программному директору',  # noqa
    ],
    [
        'Ткаченко Алексей Владимирович',
        'Директор по сбору и рециклингу текстиля',
        'Руководители и специалисты в прямом подчинении Директору',
    ],
    [
        'Трунина Елена Сергеевна',
        'HR-менеджер',
        'Отдел управления персоналом',
    ],
    [
        'Тюрин Андрей Александрович',
        'Кладовщик',
        'Центр сортировки и переработки г. Кострома',
    ],
    [
        'Тюрина Ирина Александровна',
        'Менеджер по обучению и развитию персонала',
        'Отдел управления персоналом',
    ],
    [
        'Уварова Ксения Анатольевна',
        'Email-маркетолог',
        'Отдел коммуникаций',
    ],
    [
        'Уварова Ксения Анатольевна',
        'Финансовый менеджер',
        'Финансово-административный отдел',
    ],
    [
        'Цветкова Анастасия Станиславовна',
        'Администратор',
        'Административный отдел',
    ],
    [
        'Цой Дмитрий Витальевич',
        'Заместитель директора по складской и транспортной логистике',
        'Центр сортировки г. Москва',
    ],
    [
        'Цой Лариса Владимировна',
        'Руководитель административного отдела',
        'Специалисты и подразделения в прямом подчинении Финансовому директору',  # noqa
    ],
    [
        'Чугринова Евгения Александровна',
        'Руководитель отдела по работе с партнерами',
        'Отдел по работе с партнерами',
    ],
]

CONTACT_KEYWORD_RAW = [
    [
        'Абасова Лариса Кязим кызы',
        'Лала, Юрист, Юрисконсульт, Абасова Абасова Лариса Кязим кызы Юрисконсульт',  # noqa
    ],
    [
        'Авакян Ева',
        'Ева, Авакян, Админ, администратор мастерской, SMM, СММ Авакян Ева Администратор мастерской',  # noqa
    ],
    [
        'Аверин Дмитрий Викторович',
        'Дима, Дмитрий, Аверин, Координатор, ветошь, координатор по работе с партнерами, партнерка, партнерский отдел Аверин Дмитрий Викторович Координатор отдела по работе с В2В партнерами',  # noqa
    ],
    [
        'Алексеева Дарья Владимировна',
        'Даша, Директор, Алексеева, Директор фонда Алексеева Дарья Владимировна Директор',  # noqa
    ],
    [
        'Бабайцева Юлия Олеговна',
        'Юля, Бабайцева, Юлия, Ассистент, Бизнес-ассистент Бабайцева Юлия Олеговна Бизнес-ассистент',  # noqa
    ],
    [
        'Блинова Дарья Александровна',
        'Блинова, Дарья, Даша, Менеджер, менеджерка, менеджер проектов, менеджерка проектов Блинова Дарья Александровна Менеджер проектов',  # noqa
    ],
    [
        'Васинская Яна Владимировна',
        'Васинская, Центр выдачи, Яна, ЦВ, Центр гуманитарной выдачи, Кострома Васинская Яна Владимировна Администратор центра выдачи',  # noqa
    ],
    [
        'Герасимова Инна Сергеевна',
        'Инна, Герасимова, Координатор, Координатор по работе с партнерами, партнерка, партнерский отдел Герасимова Инна Сергеевна Координатор по работе с партнерами',  # noqa
    ],
    [
        'Герасимовская Алина Алексеевна',
        'Алина, Герасимовская, Координатор, Координатор по работе с партнерами, партнерка, партнерский отдел Герасимовская Алина Алексеевна Координатор по работе с партнерами',  # noqa
    ],
    [
        'Голикова Вероника Владимировна',
        'Ника, Вероника, Голикова, Контент, контент-менеджер, пиар, PR, коммуникаций, менеджер по работе с инфлюенсерами, инфлюенсер Голикова Вероника Владимировна Контент-продюсер',  # noqa
    ],
    [
        'Гринягин Андрей Юрьевич',
        'склад, Кострома, Андрей, Гринягин, склад Кострома, директор склада, директор склада Кострома Гринягин Андрей Юрьевич Директор склада г. Кострома',  # noqa
    ],
    [
        'Двоеглазова Дарина Вячеславовна',
        'Дарина, Двоеглазова, благо, координатор благотворительный программ, координатор, программный Двоеглазова Дарина Вячеславовна Координатор благотворительных программ',  # noqa
    ],
    [
        'Дудченко Ангелина Александровна',
        'Ангелина, Гриб, Дудченко, менеджер, информационных, программ, программный Дудченко Ангелина Александровна Менеджер информационных программ',  # noqa
    ],
    [
        'Золотухина Юлия Юрьевна',
        'Юля, Юлия, ивент, event, менеджер, Золотухина, пиар, PR, коммуникаций Золотухина Юлия Юрьевна Event-менеджер',  # noqa
    ],
    [
        'Иванов (Жданов) Даниил Иванович',
        'Даня, Жданов, Иванов, медиакоординатор, пиар, PR, коммуникаций, Даниил Иванов (Жданов) Даниил Иванович Медиакоординатор',  # noqa
    ],
    [
        'Каримова Анастасия Алексеевна',
        'Настя, Каримова, Анастасия, партнерка, отдел по работе с партнерами, координатор, младший координатор Каримова Анастасия Алексеевна Ассистент отдела по работе с партнерами',  # noqa
    ],
    [
        'Кнутова Елена Геннадьевна',
        'Елена, Кнутова, Лена, Центр выдачи, ЦВ, Центр гуманитарной выдачи, Кострома Кнутова Елена Геннадьевна Координатор центра выдачи',  # noqa
    ],
    [
        'Козловских Ирина Анатольевна',
        'пиар, PR, коммуникаций, директор, Ира, Ирина, Козловских Козловских Ирина Анатольевна PR-директор',  # noqa
    ],
    [
        'Кудряшова Наталья Андреевна',
        'HR, директор, Наташа, Наталья, Кудряшова, отдел персонала, персоналом Кудряшова Наталья Андреевна HR-директор',  # noqa
    ],
    [
        'Малярова Светлана Александровна',
        'Света, Светлана, Малярова, директор склада, склад Москва, логистика, директор по логистике, Владыкино Малярова Светлана Александровна Директор по складской и транспортной логистике',  # noqa
    ],
    [
        'Матвеева Наталья Владимировна',
        'Наташа, Матвеева, Наталья, руководитель, мастерской, админ, администратор Матвеева Наталья Владимировна Руководитель мастерской г. Москва',  # noqa
    ],
    [
        'Матюхина Юлия Андреевна',
        'Юля, Юлия, Матюхина, финдир, финансовый, директор, административно-финансовый Матюхина Юлия Андреевна Финансовый директор',  # noqa
    ],
    [
        'Молчанов Иван Александрович',
        'Ваня, Косторома, Молчанов, благо, координатор благотворительный программ, координатор, программный Молчанов Иван Александрович Координатор региональных благотворительных программ',  # noqa
    ],
    [
        'Морозова Вера Юрьевна',
        'Вера, Морозова, руководитель, информационных, информационные программы, программ, программный Морозова Вера Юрьевна Руководитель отдела информационных программ',  # noqa
    ],
    [
        'Наседкина Алина Геннадьевна',
        'Алина, Наседкина, фандрайзер, пиар, PR, коммуникаций Наседкина Алина Геннадьевна Фандрайзер',  # noqa
    ],
    [
        'Обновленская Юлия Сергеевна',
        'Юля, Юлия, Обновленская, менеджер, информационных, информационные программы, программ, программный Обновленская Юлия Сергеевна Менеджер программ по обмену опытом',  # noqa
    ],
    [
        'Песоцкая Татьяна Юрьевна',
        'Таня, Татьяна, Песоцкая, директор, благо, информационных, программ, программный, информационные программы, мастерская Песоцкая Татьяна Юрьевна Программный директор',  # noqa
    ],
    [
        'Сапрыгина Мария Юрьевна',
        'Мария, Маша, Сапрыгина, бух, бухгалтер, рекло, финотдел, бухгалтерия Сапрыгина Мария Юрьевна Бухгалтер',  # noqa
    ],
    [
        'Свиридов Сергей Андреевич',
        'Сережа, Сергей, Свиридов, младший, фандрайзер, пиар, PR, коммуникаций Свиридов Сергей Андреевич Младший фандрайзер',  # noqa
    ],
    [
        'Селезнева Юлия Валерьевна',
        'Юля, Юлия, Селезнева, благо, ведущий, координатор благотворительный программ, координатор, программный Селезнева Юлия Валерьевна Ведущий координатор благотворительных программ',  # noqa
    ],
    [
        'Сиваева Екатерина Олеговна',
        'Катя, Екатерина, Сиваева, Логист, младший, логистике, склад, вывоз Сиваева Екатерина Олеговна Младший менеджер по логистике',  # noqa
    ],
    [
        'Скопенко Оксана Евгеньевна',
        'Скопенко, Оксана, Окс, бух, бухгалтер, зарплате, финотдел, бухгалтерия, кадры, по кадрам Скопенко Оксана Евгеньевна Бухгалтер по заработной плате',  # noqa
    ],
    [
        'Соркина Наталья Викторовна',
        'Наташа, Наталья, Соркина, главбух, главный, бухгалтер, финотдел, бухгалтерия, кадры, по кадрам Соркина Наталья Викторовна Главный бухгалтер',  # noqa
    ],
    [
        'Теплинская Наталья Викторовна',
        'Наташа, Наталья, руководитель, благотворительных, благо, программы, программ, программный Теплинская Наталья Викторовна Руководитель отдела благотворительных программ',  # noqa
    ],
    [
        'Ткаченко Алексей Владимирович',
        'Леша, Лёша, Ткаченко, Алексей, директор, сбору, рециклингу, текстиля, склад Ткаченко Алексей Владимирович Директор по сбору и рециклингу текстиля',  # noqa
    ],
    [
        'Трунина Елена Сергеевна',
        'HR, Лена, Елена, Трунина, менеджер, отдел персонала, персоналом, hr-менеджер Трунина Елена Сергеевна HR-менеджер',  # noqa
    ],
    [
        'Тюрин Андрей Александрович',
        'кладовщик, Кострома, Андрей, Тюрин Тюрин Андрей Александрович Кладовщик',  # noqa
    ],
    [
        'Тюрина Ирина Александровна',
        'Ира, Ирина, Тюрина, HR, менеджер, отдел персонала, персоналом, hr-менеджер, менеджер по обучению, развитию, персонала Тюрина Ирина Александровна Менеджер по обучению и развитию персонала',  # noqa
    ],
    [
        'Уварова Ксения Анатольевна',
        'Уварова, Ксюша, Ксения, менеджер, e-mail, финотдел, финансовый, менеджер, пиар, PR, коммуникаций Уварова Ксения Анатольевна Email-маркетолог Финансовый менеджер',  # noqa
    ],
    [
        'Цветкова Анастасия Станиславовна',
        'Настя, Цветкова, Анастасия, админ, администратор, офис, административный Цветкова Анастасия Станиславовна Администратор',  # noqa
    ],
    [
        'Цой Дмитрий Витальевич',
        'Цой, Дима, Дмитрий, заместитель, директора, склад, Владыкино, центр сортировки, заместитель Светы Цой Дмитрий Витальевич Заместитель директора по складской и транспортной логистике',  # noqa
    ],
    [
        'Цой Лариса Владимировна',
        'Лара, Лариса, Цой, администратор, руководитель, офис, финансово-административный, административный, административного Цой Лариса Владимировна Руководитель административного отдела',  # noqa
    ],
    [
        'Чугринова Евгения Александровна',
        'Женя, Евгения, Чугринова, руководитель, руководитель отдела, по работе с партнерами, партнерка, партнерский отдел Чугринова Евгения Александровна Руководитель отдела по работе с партнерами',  # noqa
    ],
]


async def upload_contacts():
    '''Загрузка данных в таблицу контактов.'''
    async with AsyncSessionLocal() as session:
        for contact in CONTACTS_RAW:
            new_contact = Contact()
            new_contact.full_name = contact[0]
            new_contact.phone = contact[1]
            new_contact.telegram = contact[2]
            new_contact.email = contact[3]
            session.add(new_contact)
        await session.commit()


async def upload_departments():
    '''Загрузка данных в таблицу отделос.'''
    async with AsyncSessionLocal() as session:
        for department in DEPARTMENTS_RAW:
            new_department = Department()
            new_department.name = department
            session.add(new_department)
        await session.commit()


async def upload_job_titles():
    '''Загрузка данных в таблицу должностей.'''
    async with AsyncSessionLocal() as session:
        for job_title in JOB_TITLES_RAW:
            new_job_title = JobTitle()
            new_job_title.name = job_title
            session.add(new_job_title)
        await session.commit()


async def upload_department_job_title():
    '''Загрузка данных в таблицу связи отделов и должностей.'''
    for job_title, department in DEPARTMENT_JOB_TITLE_RAW:
        async with AsyncSessionLocal() as session:
            department_id = await session.execute(
                select(Department.id).where(Department.name == department)
            )
            job_title_id = await session.execute(
                select(JobTitle.id).where(JobTitle.name == job_title)
            )
            department_id = department_id.scalars().first()
            job_title_id = job_title_id.scalars().first()

            new_department_job_title = DepartmentJobTitle()
            new_department_job_title.department_id = department_id
            new_department_job_title.job_title_id = job_title_id
            session.add(new_department_job_title)
            await session.commit()


async def upload_position():
    '''Загрузка данных в таблицу занимаемых должностей контактами.'''
    for full_name, job_title, department in POSITION_RAW:
        async with AsyncSessionLocal() as session:
            contact_id = await session.execute(
                select(Contact.id).where(Contact.full_name == full_name)
            )
            contact_id = contact_id.scalars().first()
            job_title_id = await session.execute(
                select(JobTitle.id).where(JobTitle.name == job_title)
            )
            job_title_id = job_title_id.scalars().first()
            department_id = await session.execute(
                select(Department.id).where(Department.name == department)
            )
            department_id = department_id.scalars().first()
            department_job_title_id = await session.execute(
                select(DepartmentJobTitle.id).where(
                    DepartmentJobTitle.department_id == department_id,
                    DepartmentJobTitle.job_title_id == job_title_id,
                )
            )
            department_job_title_id = department_job_title_id.scalars().first()
            new_position = Position()
            new_position.contact_id = contact_id
            new_position.department_job_title_id = department_job_title_id
            session.add(new_position)
            await session.commit()


async def upload_contact_keyword():
    '''
    Загрузка данных в таблицы:
    - ключевых слов;
    - связи ключевых слов с контактами.
    '''
    for full_name, keywords in CONTACT_KEYWORD_RAW:
        keywords = prepare_words(keywords)
        async with AsyncSessionLocal() as session:
            contact_id = await session.execute(
                select(Contact.id).where(Contact.full_name == full_name)
            )
            contact_id = contact_id.scalars().first()
            for keyword in keywords:
                keyword_id = await session.execute(
                    select(Keyword.id).where(Keyword.name == keyword)
                )
                keyword_id = keyword_id.scalars().first()
                if not keyword_id:
                    keyword_db = Keyword()
                    keyword_db.name = keyword
                    session.add(keyword_db)
                    await session.commit()
                    await session.refresh(keyword_db)
                    keyword_id = keyword_db.id
                contact_keyword = ContactKeyword()
                contact_keyword.contact_id = contact_id
                contact_keyword.keyword_id = keyword_id
                session.add(contact_keyword)
                await session.commit()


async def main():
    '''Последовательная загрузка данных в таблицы.'''
    await upload_contacts()
    await upload_departments()
    await upload_job_titles()
    await upload_department_job_title()
    await upload_position()
    await upload_contact_keyword()


if __name__ == '__main__':
    print('Начинаю заполнять БД информацией о контактах...')
    asyncio.run(main())
    print('Готово!')
