%define enable_gnometris 1

%define schemas aisleriot blackjack glines gnect gnibbles gnobots2 gnometris gnomine gnotravex gnotski gtali iagno mahjongg same-gnome glchess

%define gamesdir	%{_localstatedir}/games

Summary:	GNOME games
Name:		gnome-games
Version: 2.19.3
Release: %mkrel 2
License:	GPL
Group:		Games/Other

Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-games/gnome-games-%{version}.tar.bz2
Source6:	%{name}-icons16.tar.bz2
Source7:	%{name}-icons32.tar.bz2
Source8:	%{name}-icons48.tar.bz2
BuildRequires:	gettext
BuildRequires:	guile-devel
BuildRequires:	libgnomeui2-devel >= 2.0.0
Buildrequires:  libglade2.0-devel
BuildRequires:  gtk+2-devel >= 2.5.4
BuildRequires:  libexpat-devel
BuildRequires:	scrollkeeper
BuildRequires:	gnome-doc-utils
Buildrequires:  librsvg-devel
Buildrequires:  pygtk2.0-devel gnome-python-desktop
Buildrequires:  avahi-glib-devel avahi-client-devel
Buildrequires:  libgstreamer0.10-devel
Buildrequires:  libgcrypt-devel
Buildrequires:  perl-XML-Parser
BuildRequires:  gob2
BuildRequires:  automake1.7
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	desktop-file-utils

BuildRoot:	%{_tmppath}/%{name}-%{version}-root
URL:		http://www.gnome.org/projects/gnome-games/
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

%description
The gnome-games package includes games for the GNOME GUI desktop environment.
They include:

AisleRiot       A compilation of seventy different solitaire card games.
Ataxx           Disk-flipping game where players try and control most disks.
Blackjack       The famous casino card game without any need to pay.
Four-in-a-row   Players tries to make a line of four disks. (Connect Four)
Gnometris       Tetris clone.
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


%prep
%setup -q

%build
%configure2_5x --enable-compile-warnings=no
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang

GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

%if !%enable_gnometris
rm -rf  $RPM_BUILD_ROOT%{_datadir}/applications/gnometris.desktop \
  $RPM_BUILD_ROOT%{_datadir}/pixmaps/gnome-gtetris.png \
  $RPM_BUILD_ROOT%{_datadir}/pixmaps/gnometris \
  $RPM_BUILD_ROOT%{gamesdir}/gnometris.scores
%endif

install -m 755 -d $RPM_BUILD_ROOT%{_menudir}
cat << EOF >> $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): title="GNOME Mines" longtitle="Mines game" command="%{_bindir}/gnomine" icon="gnome-gnomine.png" needs="x11" section="More Applications/Games/Puzzles" startup_notify="true" xdg="true"
?package(%{name}): title="Same GNOME" longtitle="GNOME SameGame" command="%{_bindir}/same-gnome" icon="gnome-gsame.png" needs="x11" section="More Applications/Games/Other" startup_notify="true" xdg="true"
?package(%{name}): title="GNOME Mahjongg" longtitle="Mahjongg game" command="%{_bindir}/mahjongg" icon="gnome-mahjongg.png" kde_info="GNOME Mahjongg game" needs="x11" section="More Applications/Games/Puzzles" startup_notify="true" xdg="true"
?package(%{name}): title="GTali" longtitle="Poker-like dice game" command="%{_bindir}/gtali" icon="gnome-gtali.png" needs="x11" section="More Applications/Games/Other" start_notify="true" xdg="true"
?package(gnome-games): title="GNOME Robots" longtitle="GNOME Robots game" command="%{_bindir}/gnobots2" icon="gnome-gnobots.png" needs="x11" section="More Applications/Games/Arcade" startup_notify="true" xdg="true"
?package(%{name}): icon="iagno.png" title="Iagno" longtitle="Reversi chess" command="%{_bindir}/iagno" needs="x11" section="More Applications/Games/Boards" startup_notify="true" xdg="true"
?package(%{name}): title="GNOME Tetravex" longtitle="Tetravex puzzle" command="%{_bindir}/gnotravex" icon="gnome-gnotravex.png" needs="x11" section="More Applications/Games/Puzzles" startup_notify="true" xdg="true"
?package(%{name}): title="AisleRiot" longtitle="Card-based Solitaire suite" command="%{_bindir}/sol" icon="gnome-aisleriot.png" needs="x11" section="More Applications/Games/Cards" startup_notify="true" xdg="true"
?package(%{name}): title="Glines" longtitle="Color lines chess" command="%{_bindir}/glines" icon="glines.png" needs="x11" section="More Applications/Games/Boards" startup_notify="true" xdg="true"
?package(gnome-games): title="Gnibbles" longtitle="Nibbles Game" command="%{_bindir}/gnibbles" icon="gnome-nibbles.png" needs="x11" icon="gnome-nibbles.png" section="More Applications/Games/Arcade" startup_notify="true" xdg="true"
?package(%{name}): title="Gnect" longtitle="Four-in-a-row chess" command="%{_bindir}/gnect" needs="x11" section="More Applications/Games/Boards" icon="gnect-icon.png" startup_notify="true" xdg="true"
?package(%{name}): title="Gnometris" longtitle="Tetris game" command="%{_bindir}/gnometris" icon="gnome-gtetris.png" needs="x11" section="More Applications/Games/Arcade" startup_notify="true" xdg="true"
?package(%{name}): title="Blackjack" longtitle="Blackjack" command="%{_bindir}/blackjack" icon="gnome-blackjack.png" needs="x11" section="More Applications/Games/Cards" startup_notify="true" xdg="true"
EOF
desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-MoreApplications-Games-Puzzles" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/{gnomine.desktop,mahjongg.desktop,gnotravex.desktop,gnome-sudoku.desktop}
desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-MoreApplications-Games-Other" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/{same-gnome.desktop,gtali.desktop}
desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-MoreApplications-Games-Arcade" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/{gnobots2.desktop,gnometris.desktop}
desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-MoreApplications-Games-Boards" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/{iagno.desktop,glines.desktop,gnect.desktop,glchess.desktop}
desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-MoreApplications-Games-Cards" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/{sol.desktop,blackjack.desktop}

mkdir -p $RPM_BUILD_ROOT%{_miconsdir} $RPM_BUILD_ROOT%{_iconsdir} $RPM_BUILD_ROOT%{_liconsdir}

bzcat %{SOURCE6} | tar xf - -C $RPM_BUILD_ROOT%{_miconsdir}
bzcat %{SOURCE7} | tar xf - -C $RPM_BUILD_ROOT%{_iconsdir}
bzcat %{SOURCE8} | tar xf - -C $RPM_BUILD_ROOT%{_liconsdir}

%{find_lang} %{name} --with-gnome --all-name
for omf in %buildroot%_datadir/omf/*/*-{??,??_??}.omf; do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done

rm -rf %buildroot/var/lib/scrollkeeper

%clean
rm -rf $RPM_BUILD_ROOT

%post
%post_install_gconf_schemas %schemas
%update_scrollkeeper
%{update_menus}
%update_icon_cache hicolor

%preun
%preun_uninstall_gconf_schemas %schemas

%postun
%clean_scrollkeeper
%{clean_menus}
%clean_icon_cache hicolor

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
	gnometris \
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
	same-gnome.Small \
	same-gnome.Medium \
	same-gnome.Large \
; do
	%create_ghostfile %{gamesdir}/$i.scores games games 0664
	if [ -f "%{gamesdir}/$i.scores" -a ! -s "%{gamesdir}/$i.scores" ]; then
	echo "0.000000 `date +%s` gnome" >> %{gamesdir}/$i.scores
	fi
done

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS TODO
%{_sysconfdir}/gconf/schemas/aisleriot.schemas
%{_sysconfdir}/gconf/schemas/blackjack.schemas
%{_sysconfdir}/gconf/schemas/glchess.schemas
%{_sysconfdir}/gconf/schemas/glines.schemas
%{_sysconfdir}/gconf/schemas/gnect.schemas
%{_sysconfdir}/gconf/schemas/gnibbles.schemas
%{_sysconfdir}/gconf/schemas/gnobots2.schemas
%{_sysconfdir}/gconf/schemas/gnometris.schemas
%{_sysconfdir}/gconf/schemas/gnomine.schemas
%{_sysconfdir}/gconf/schemas/gnotravex.schemas
%{_sysconfdir}/gconf/schemas/gnotski.schemas
%{_sysconfdir}/gconf/schemas/gtali.schemas
%{_sysconfdir}/gconf/schemas/iagno.schemas
%{_sysconfdir}/gconf/schemas/mahjongg.schemas
%{_sysconfdir}/gconf/schemas/same-gnome.schemas

%{_bindir}/sol
%{_bindir}/gnect
%{_bindir}/blackjack
%{_bindir}/gnome-gnuchess
%{_bindir}/glchess
%{_bindir}/gnome-sudoku

# these are setgid games so they can write in score files
%defattr(2555, root, games)
%if %enable_gnometris
%{_bindir}/gnometris
%endif
%{_bindir}/glines
%{_bindir}/gnibbles
%{_bindir}/gnobots2
%{_bindir}/gnomine
%{_bindir}/gnotravex
%{_bindir}/gnotski
%{_bindir}/gtali
%{_bindir}/iagno
%{_bindir}/mahjongg
%{_bindir}/same-gnome

%defattr(-, root, root)
%py_puresitedir/glchess
%py_puresitedir/gnome_sudoku
%_datadir/icons/hicolor/*/apps/*
%{_datadir}/applications/*
%{_datadir}/ggz
%{_datadir}/glchess
%{_datadir}/gnome-games
%{_datadir}/gnome-sudoku
%{_datadir}/gnect
%{_datadir}/gnibbles
%{_datadir}/gnobots2
%{_datadir}/pixmaps/*
%{_menudir}/*
%{_iconsdir}/*.png
%{_liconsdir}/*.png
%{_miconsdir}/*.png
%attr(664, games, games) %ghost %{gamesdir}/*
%dir %{_datadir}/omf/%name
%{_datadir}/omf/*/*-C.omf
%_datadir/gnome-games-common/
%_libdir/gnome-games
