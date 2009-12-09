
%define schemas aisleriot glines gnect gnibbles gnobots2 gnome-sudoku gnomine gnotravex gnotski gtali iagno lightsoff mahjongg glchess quadrapassel swell-foop

%define gamesdir	%{_localstatedir}/games

%define build_staging 0

Summary:	GNOME games
Name:		gnome-games
Version: 2.29.3
Release: %mkrel 1
License:	GPLv2+
Group:		Games/Other

Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-games/gnome-games-%{version}.tar.bz2
Patch: gnome-games-2.29.2-fix-linking.patch
BuildRequires:	gettext
BuildRequires:	guile-devel
BuildRequires:  gtk+2-devel >= 2.5.4
BuildRequires:  libGConf2-devel
#gw libtool dep
BuildRequires:  dbus-glib-devel
BuildRequires:  libexpat-devel
BuildRequires:	scrollkeeper
BuildRequires:	gnome-doc-utils
Buildrequires:  librsvg-devel
Buildrequires:  pygtk2.0-devel gnome-python-desktop
Buildrequires:  avahi-glib-devel avahi-client-devel
Buildrequires:  libSDL_mixer-devel
Buildrequires:  libgcrypt-devel
BuildRequires:	intltool
BuildRequires:  gob2
BuildRequires:  automake1.7
BuildRequires:	gnome-common
BuildRequires:	desktop-file-utils
BuildRequires:	libcanberra-devel
BuildRequires:	clutter-devel >= 1.0
BuildRequires:	clutter-gtk-devel >= 0.10
BuildRequires:	gobject-introspection-devel gir-repository
BuildRequires:	x11-server-xvfb

BuildRoot:	%{_tmppath}/%{name}-%{version}-root
URL:		http://live.gnome.org/GnomeGames/
Requires:	guile
Requires(post):	scrollkeeper >= 0.3
Requires(postun):scrollkeeper >= 0.3
Requires(pre):	rpm-helper
Requires:	librsvg
Requires: gnome-python-gnomeprint gnome-python
Requires: python-gtkglext
Requires: pygtk2.0-libglade
Requires: gnome-python-gconf
Requires: gnome-python-gnomevfs
Provides: glchess
Obsoletes: glchess
Requires(post): ggz-client-libs
Requires(preun): ggz-client-libs
Requires: seed

%description
The gnome-games package includes games for the GNOME GUI desktop environment.
They include:

AisleRiot       A compilation of seventy different solitaire card games.
Ataxx           Disk-flipping game where players try and control most disks.
Four-in-a-row   Players tries to make a line of four disks. (Connect Four)
Iagno           GNOME version of the popular Othello (R) chess.
Klotski         A series of sliding block puzzles.
Lines           Move balls around the grid to form lines of the same colour
                to make them disappear, while more balls keep dropping in.
Mahjongg        Remove tiles in matching pairs from a pile to dismantle it.
Mines           The popular logic puzzle minesweeper.
Nibbles         Pilot a worm around a maze trying to collect diamonds.
Robots          Classic BSD robots game, avoiding robots approaching you.
Same GNOME      In a grid of stones of different colors, try remove stones
                where two or more of the same colour touch each other.
Tali            Poker-like dice game without money, similar to Yahtzee.
Tetravex        A puzzle where you match tiles edges together.
GLChess		Chess with a 3D board.
Lights Off	Turn off all the lights.
Swell Foop	Clear the screen by removing groups of colored and shaped tiles
Quadrapassel	Tetris clone.

%package devel
Group: Development/Other
Summary: Gnome games library introspection
Requires: %name = %version-%release

%description devel
This contains GObject-Introspection support for the libraries of %name.


%prep
%setup -q
%patch -p1
autoreconf -fi

%build
%configure2_5x --enable-compile-warnings=no \
%if %build_staging
--enable-staging \
%endif
--enable-aisleriot-clutter

%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang

GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

%{find_lang} %{name} --with-gnome --all-name
for omf in %buildroot%_datadir/omf/*/*-{??,??_??}.omf; do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done

rm -rf %buildroot/var/lib/scrollkeeper $RPM_BUILD_ROOT%{_sysconfdir}/ggz.modules

%check
xvfb-run make check

%clean
rm -rf $RPM_BUILD_ROOT

%post
%if %mdkversion < 200900
%post_install_gconf_schemas %schemas
%update_scrollkeeper
%{update_menus}
%update_icon_cache hicolor
%endif

%preun
%preun_uninstall_gconf_schemas %schemas


%if %mdkversion < 200900
%postun
%clean_scrollkeeper
%{clean_menus}
%clean_icon_cache hicolor
%endif

%pre
[ -d %{gamesdir} ] || mkdir -p %{gamesdir}
for i in \
	glines.Small \
	glines.Medium \
	glines.Large \
	glines.Custom \
	gnibbles.1.0 \
	gnibbles.1.1 \
	gnibbles.2.0 \
	gnibbles.2.1 \
	gnibbles.3.0 \
	gnibbles.3.1 \
	gnibbles.4.0 \
	gnibbles.4.1 \
	gnobots2.classic_robots-safe \
	gnobots2.classic_robots \
	gnobots2.classic_robots-super-safe \
	gnobots2.nightmare-safe \
	gnobots2.nightmare \
	gnobots2.nightmare-super-safe \
	gnobots2.robots2_easy-safe \
	gnobots2.robots2_easy \
	gnobots2.robots2_easy-super-safe \
	gnobots2.robots2-safe \
	gnobots2.robots2 \
	gnobots2.robots2-super-safe \
	gnobots2.robots_with_safe_teleport-safe \
	gnobots2.robots_with_safe_teleport \
	gnobots2.robots_with_safe_teleport-super-safe \
	gnomine.Custom \
	gnomine.Large \
	gnomine.Medium \
	gnomine.Small \
	gnotravex.2x2 \
	gnotravex.3x3 \
	gnotravex.4x4 \
	gnotravex.5x5 \
	gnotravex.6x6 \
	gnotski.10 \
	gnotski.11 \
	gnotski.12 \
	gnotski.13 \
	gnotski.14 \
	gnotski.15 \
	gnotski.16 \
	gnotski.17 \
	gnotski.1 \
	gnotski.20 \
	gnotski.21 \
	gnotski.22 \
	gnotski.23 \
	gnotski.24 \
	gnotski.25 \
	gnotski.26 \
	gnotski.27 \
	gnotski.28 \
	gnotski.29 \
	gnotski.2 \
	gnotski.30 \
	gnotski.31 \
	gnotski.32 \
	gnotski.33 \
	gnotski.34 \
	gnotski.35 \
	gnotski.36 \
	gnotski.37 \
	gnotski.3 \
	gnotski.4 \
	gnotski.5 \
	gnotski.6 \
	gnotski.7 \
	gnotski.8 \
	gnotski.9 \
	gtali.Regular \
	gtali.Colors \
	mahjongg.easy \
	mahjongg.difficult \
	mahjongg.confounding \
	mahjongg.pyramid \
	mahjongg.tictactoe \
	mahjongg.cloud \
	mahjongg.dragon \
	mahjongg.bridges \
	mahjongg.ziggurat \
; do
	%create_ghostfile %{gamesdir}/$i.scores games games 0664
	if [ -f "%{gamesdir}/$i.scores" -a ! -s "%{gamesdir}/$i.scores" ]; then
	echo "0.000000 `date +%s` gnome" >> %{gamesdir}/$i.scores
	fi
done

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS NEWS TODO
%{_sysconfdir}/gconf/schemas/aisleriot.schemas
%{_sysconfdir}/gconf/schemas/glchess.schemas
%{_sysconfdir}/gconf/schemas/glines.schemas
%{_sysconfdir}/gconf/schemas/gnect.schemas
%{_sysconfdir}/gconf/schemas/gnibbles.schemas
%{_sysconfdir}/gconf/schemas/gnobots2.schemas
%{_sysconfdir}/gconf/schemas/gnome-sudoku.schemas
%{_sysconfdir}/gconf/schemas/gnomine.schemas
%{_sysconfdir}/gconf/schemas/gnotravex.schemas
%{_sysconfdir}/gconf/schemas/gnotski.schemas
%{_sysconfdir}/gconf/schemas/gtali.schemas
%{_sysconfdir}/gconf/schemas/iagno.schemas
%{_sysconfdir}/gconf/schemas/lightsoff.schemas
%{_sysconfdir}/gconf/schemas/mahjongg.schemas
%{_sysconfdir}/gconf/schemas/quadrapassel.schemas
%{_sysconfdir}/gconf/schemas/swell-foop.schemas
%{_bindir}/sol
%{_bindir}/gnect
%{_bindir}/gnome-gnuchess
%{_bindir}/glchess
%{_bindir}/gnome-sudoku
%{_bindir}/lightsoff

# these are setgid games so they can write in score files
%defattr(2555, root, games)
%{_bindir}/quadrapassel
%{_bindir}/glines
%{_bindir}/gnibbles
%{_bindir}/gnobots2
%{_bindir}/gnomine
%{_bindir}/gnotravex
%{_bindir}/gnotski
%{_bindir}/gtali
%{_bindir}/iagno
%{_bindir}/mahjongg
%{_bindir}/swell-foop

%defattr(-, root, root)
%py_puresitedir/glchess
%py_puresitedir/gnome_sudoku
%_datadir/icons/hicolor/*/apps/*
%{_datadir}/applications/*
%{_datadir}/glchess
%{_datadir}/gnome-games
%{_datadir}/gnome-sudoku
%attr(664, games, games) %ghost %{gamesdir}/*
%dir %{_datadir}/omf/*
%{_datadir}/omf/*/*-C.omf
%_datadir/gnome-games-common/
%_mandir/man6/*.6*
%_libdir/gnome-games
%_libdir/girepository-1.0/GnomeGamesSupport-1.0.typelib

%files devel
%defattr(-, root, root)
%_datadir/gir-1.0/GnomeGamesSupport-1.0.gir
