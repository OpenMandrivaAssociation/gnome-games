Summary:	GNOME games
Name:		gnome-games
Version:	3.2.1
Release:	3
License:	GPLv2+
Group:		Games/Other
URL:		http://live.gnome.org/GnomeGames/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-games/gnome-games-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	gnome-doc-utils
BuildRequires:  gob2
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	x11-server-xvfb
BuildRequires:	vala
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(gobject-introspection-1.0)

#Requires: aisleriot
Requires: glchess
Requires: glines
Requires: gnect
Requires: gnibbles
Requires: gnobots2
Requires: gnome-mahjongg
Requires: gnome-sudoku
Requires: gnomine
Requires: gnotravex
Requires: gnotski
Requires: gtali
Requires: iagno
Obsoletes: lightsoff
Requires: quadrapassel
Obsoletes: swell-foop

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

#-----------------------------------------------------------
%package common
Summary: Common files for GNOME Games
Group: Games/Other
Conflicts: gnome-games < 2.29.6-2

%description common
Common files for GNOME Games.

%files common -f %{name}.lang
%{_libdir}/gnome-games/libgames-support-gi.so.*
%{_libdir}/gnome-games/GnomeGamesSupport-1.0.typelib
%{_datadir}/glib-2.0/schemas/org.gnome.Games.WindowState.gschema.xml
%dir %{_datadir}/gnome-games
%{_datadir}/gnome-games/sounds 
%{_datadir}/gnome-games/pixmaps 

#-----------------------------------------------------------
%package -n glchess
Summary: Chess with a 3D board
Group: Games/Other
Conflicts: gnome-games < 2.29.6-2
Requires: %{name}-common = %{version}-%{release}

%description -n glchess
Chess with a 3D board.

%files -n glchess -f glchess.lang
%attr(2555, root, games) %{_bindir}/glchess
%attr(2555, root, games) %{_bindir}/gnome-gnuchess
%{_datadir}/glchess
%{_datadir}/applications/glchess.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.glchess.gschema.xml
%{_iconsdir}/*/*/*/*glchess.*
%{_mandir}/man6/glchess.*

#-----------------------------------------------------------
%package -n glines
Summary: Move balls
Group: Games/Other
Conflicts: gnome-games < 2.29.6-2
Requires: %{name}-common = %{version}-%{release}

%description -n glines
Move balls around the grid to form lines of the same colour
to make them disappear, while more balls keep dropping in.

%pre -n glines
[ -d %{_localstatedir}/games ] || mkdir -p %{_localstatedir}/games
for i in glines.Large \
  glines.Medium \
  glines.Small \
; do
  %create_ghostfile %{_localstatedir}/games/$i.scores games games 0664
  if [ -f "%{_localstatedir}/games/$i.scores" -a ! -s "%{_localstatedir}/games/$i.scores" ]; then
    echo "0.000000 `date +%s` gnome" >> %{_localstatedir}/games/$i.scores
  fi
done

%files -n glines -f glines.lang
%attr(2555, root, games) %{_bindir}/glines
%{_datadir}/gnome-games/glines
%{_datadir}/applications/glines.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.glines.gschema.xml
%{_iconsdir}/*/*/*/*glines.*
%{_mandir}/man6/glines.*
%attr(664, games, games) %ghost %{_localstatedir}/games/glines.*.scores

#-----------------------------------------------------------
%package -n gnect
Summary: A four-in-a-row game
Group: Games/Other
Conflicts: gnome-games < 2.29.6-2
Requires: %{name}-common = %{version}-%{release}

%description -n gnect
gnect is a four-in-a-row game for the GNOME Project.
The object of the game is to build a line of four of your marbles
while trying to stop your opponent (human or computer) building a
line of his or her own. A line can be horizontal, vertical or
diagonal.

%files -n gnect -f gnect.lang
%{_sysconfdir}/gconf/schemas/gnect.schemas
%attr(2555, root, games) %{_bindir}/gnect
%{_datadir}/gnome-games/gnect
%{_datadir}/applications/gnect.desktop
#{_datadir}/glib-2.0/schemas/org.gnome.gnect.gschema.xml
%{_iconsdir}/*/*/*/*gnect.*
%{_mandir}/man6/gnect.*

#-----------------------------------------------------------
%package -n gnibbles
Summary: A worm game
Group: Games/Other
Conflicts: gnome-games < 2.29.6-2
Requires: %{name}-common = %{version}-%{release}

%description -n gnibbles
Nibbles is a worm game for GNOME. The player controls a 2D
worm while trying to get food. Getting food gives points,
but hitting anything causes a loss of points. When all points
are lost, the player loses.

%pre -n gnibbles
[ -d %{_localstatedir}/games ] || mkdir -p %{_localstatedir}/games
for i in \
  gnibbles.1.0 \
  gnibbles.1.1 \
  gnibbles.2.0 \
  gnibbles.2.1 \
  gnibbles.3.0 \
  gnibbles.3.1 \
  gnibbles.4.0 \
  gnibbles.4.1 \
; do
  %create_ghostfile %{_localstatedir}/games/$i.scores games games 0664
  if [ -f "%{_localstatedir}/games/$i.scores" -a ! -s "%{_localstatedir}/games/$i.scores" ]; then
    echo "0.000000 `date +%s` gnome" >> %{_localstatedir}/games/$i.scores
  fi
done

%files -n gnibbles -f gnibbles.lang
%{_sysconfdir}/gconf/schemas/gnibbles.schemas
%attr(2555, root, games) %{_bindir}/gnibbles
%{_datadir}/gnome-games/gnibbles
%{_datadir}/applications/gnibbles.desktop
#{_datadir}/glib-2.0/schemas/org.gnome.gnibbles.gschema.xml
%{_iconsdir}/*/*/*/*gnibbles.*
%{_mandir}/man6/gnibbles.*
%attr(664, games, games) %ghost %{_localstatedir}/games/gnibbles.*.scores

#-----------------------------------------------------------
%package -n gnobots2
Summary: Graphical version of text based robots game
Group: Games/Other
Conflicts: gnome-games < 2.29.6-2
Requires: %{name}-common = %{version}-%{release}

%description -n gnobots2
Robots is a graphical version of the original text based
robots game, which can be found on a number of UNIX systems.
The player must outwit the robots chasing him/her by getting
them to run into each other.

%pre -n gnobots2
[ -d %{_localstatedir}/games ] || mkdir -p %{_localstatedir}/games
for i in \
	gnobots2.classic_robots-safe \
	gnobots2.classic_robots-super-safe \
	gnobots2.classic_robots \
	gnobots2.nightmare-safe \
	gnobots2.nightmare-super-safe \
	gnobots2.nightmare \
	gnobots2.robots2-safe \
	gnobots2.robots2-super-safe \
	gnobots2.robots2 \
	gnobots2.robots2_easy-safe \
	gnobots2.robots2_easy-super-safe \
	gnobots2.robots2_easy \
	gnobots2.robots_with_safe_teleport-safe \
	gnobots2.robots_with_safe_teleport-super-safe \
	gnobots2.robots_with_safe_teleport \
; do
  %create_ghostfile %{_localstatedir}/games/$i.scores games games 0664
  if [ -f "%{_localstatedir}/games/$i.scores" -a ! -s "%{_localstatedir}/games/$i.scores" ]; then
    echo "0.000000 `date +%s` gnome" >> %{_localstatedir}/games/$i.scores
  fi
done

%files -n gnobots2 -f gnobots2.lang
%{_sysconfdir}/gconf/schemas/gnobots2.schemas
%attr(2555, root, games) %{_bindir}/gnobots2
%{_datadir}/gnome-games/gnobots2
%{_datadir}/applications/gnobots2.desktop
#{_datadir}/glib-2.0/schemas/org.gnome.gnobots2.gschema.xml
%{_iconsdir}/*/*/*/*robots.*
%{_datadir}/gnome-games/icons/hicolor/*/actions/teleport*.png
%{_mandir}/man6/gnobots2.*
%attr(664, games, games) %ghost %{_localstatedir}/games/gnobots2.*.scores

#-----------------------------------------------------------
%package -n gnome-sudoku
Summary: Generate and play the popular Sudoku logic puzzle
Group: Games/Other
Conflicts: gnome-games < 2.29.6-2
Requires: %{name}-common = %{version}-%{release}

%description -n gnome-sudoku
gnome-sudoku is an application to generate and play the popular
Sudoku logic puzzle (also known as Number Place).

%files -n gnome-sudoku -f gnome-sudoku.lang
%{_sysconfdir}/gconf/schemas/gnome-sudoku.schemas
%attr(2555, root, games) %{_bindir}/gnome-sudoku
%{py_puresitedir}/gnome_sudoku
%{_datadir}/gnome-sudoku
%{_datadir}/applications/gnome-sudoku.desktop
#{_datadir}/glib-2.0/schemas/org.gnome.gnome-sudoku.gschema.xml
%{_iconsdir}/*/*/*/gnome-sudoku.*
%{_mandir}/man6/gnome-sudoku.*

#-----------------------------------------------------------
%package -n gnomine
Summary: A puzzle game
Group: Games/Other
Conflicts: gnome-games < 2.29.6-2
Requires: %{name}-common = %{version}-%{release}

%description -n gnomine
gnomine is a puzzle game where you locate mines floating in an
ocean using only your brain and a little bit of luck.

%pre -n gnomine
[ -d %{_localstatedir}/games ] || mkdir -p %{_localstatedir}/games
for i in \
  gnomine.Custom \
  gnomine.Large \
  gnomine.Medium \
  gnomine.Small \
; do
  %create_ghostfile %{_localstatedir}/games/$i.scores games games 0664
  if [ -f "%{_localstatedir}/games/$i.scores" -a ! -s "%{_localstatedir}/games/$i.scores" ]; then
    echo "0.000000 `date +%s` gnome" >> %{_localstatedir}/games/$i.scores
  fi
done

%files -n gnomine -f gnomine.lang
%attr(2555, root, games) %{_bindir}/gnomine
%{_datadir}/gnome-games/gnomine
%{_datadir}/applications/gnomine.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnomine.gschema.xml
%{_iconsdir}/*/*/*/gnomine.*
%{_mandir}/man6/gnomine.*
%attr(664, games, games) %ghost %{_localstatedir}/games/gnomine.*.scores

#-----------------------------------------------------------
%package -n gnotravex
Summary: A simple puzzle game
Group: Games/Other
Conflicts: gnome-games < 2.29.6-2
Requires: %{name}-common = %{version}-%{release}

%description -n gnotravex
GNOME Tetravex is a simple puzzle where pieces must be positioned so
that the same numbers are touching each other. Your game is timed,
these times are stored in a system-wide scoreboard.

%pre -n gnotravex
[ -d %{_localstatedir}/games ] || mkdir -p %{_localstatedir}/games
for i in \
  gnotravex.2x2 \
  gnotravex.3x3 \
  gnotravex.4x4 \
  gnotravex.5x5 \
  gnotravex.6x6 \
; do
  %create_ghostfile %{_localstatedir}/games/$i.scores games games 0664
  if [ -f "%{_localstatedir}/games/$i.scores" -a ! -s "%{_localstatedir}/games/$i.scores" ]; then
    echo "0.000000 `date +%s` gnome" >> %{_localstatedir}/games/$i.scores
  fi
done

%files -n gnotravex -f gnotravex.lang
%attr(2555, root, games) %{_bindir}/gnotravex
%{_datadir}/applications/gnotravex.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnotravex.gschema.xml
%{_iconsdir}/*/*/*/*tetravex.*
%{_mandir}/man6/gnotravex.*
%attr(664, games, games) %ghost %{_localstatedir}/games/gnotravex.*.scores

#-----------------------------------------------------------
%package -n gnotski
Summary: Clone of the Klotski game
Group: Games/Other
Conflicts: gnome-games < 2.29.6-2
Requires: %{name}-common = %{version}-%{release}

%description -n gnotski
The gnotski application is a clone of the Klotski game. The
objective is to move the patterned block to the area bordered
by green markers.

%pre -n gnotski
[ -d %{_localstatedir}/games ] || mkdir -p %{_localstatedir}/games
for i in \
  gnotski.1 \
  gnotski.2 \
  gnotski.3 \
  gnotski.4 \
  gnotski.5 \
  gnotski.6 \
  gnotski.7 \
  gnotski.8 \
  gnotski.9 \
  gnotski.10 \
  gnotski.11 \
  gnotski.12 \
  gnotski.13 \
  gnotski.14 \
  gnotski.15 \
  gnotski.16 \
  gnotski.17 \
  gnotski.18 \
  gnotski.19 \
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
  gnotski.30 \
  gnotski.31 \
  gnotski.32 \
  gnotski.33 \
  gnotski.34 \
  gnotski.35 \
  gnotski.36 \
  gnotski.37 \
; do
  %create_ghostfile %{_localstatedir}/games/$i.scores games games 0664
  if [ -f "%{_localstatedir}/games/$i.scores" -a ! -s "%{_localstatedir}/games/$i.scores" ]; then
    echo "0.000000 `date +%s` gnome" >> %{_localstatedir}/games/$i.scores
  fi
done

%files -n gnotski -f gnotski.lang
%{_sysconfdir}/gconf/schemas/gnotski.schemas
%attr(2555, root, games) %{_bindir}/gnotski
%{_datadir}/gnome-games/gnotski
%{_datadir}/applications/gnotski.desktop
#{_datadir}/glib-2.0/schemas/org.gnome.gnotski.gschema.xml
%{_iconsdir}/*/*/*/*klotski.*
%{_mandir}/man6/gnotski.*
%attr(664, games, games) %ghost %{_localstatedir}/games/gnotski.*.scores

#-----------------------------------------------------------
%package -n gtali
Summary: Tali is like Yahtzee for GNOME
Group: Games/Other
Conflicts: gnome-games < 2.29.6-2
Requires: %{name}-common = %{version}-%{release}

%description -n gtali
Tali is like Yahtzee for GNOME or like poker with dice. The player
rolls dice to try to make the best possible combinations, like
4 of a kind, small straight, and full house. The player is allowed
3 rolls per turn and can hold certain dice with each roll.

%pre -n gtali
[ -d %{_localstatedir}/games ] || mkdir -p %{_localstatedir}/games
for i in \
  gtali.Colors \
  gtali.Regular \
; do
  %create_ghostfile %{_localstatedir}/games/$i.scores games games 0664
  if [ -f "%{_localstatedir}/games/$i.scores" -a ! -s "%{_localstatedir}/games/$i.scores" ]; then
    echo "0.000000 `date +%s` gnome" >> %{_localstatedir}/games/$i.scores
  fi
done

%files -n gtali -f gtali.lang
%{_sysconfdir}/gconf/schemas/gtali.schemas
%attr(2555, root, games) %{_bindir}/gtali
%{_datadir}/gnome-games/gtali
%{_datadir}/applications/gtali.desktop
#{_datadir}/glib-2.0/schemas/org.gnome.gtali.gschema.xml
%{_iconsdir}/*/*/*/*tali.*
%{_mandir}/man6/gtali.*
%attr(664, games, games) %ghost %{_localstatedir}/games/gtali.*.scores

#-----------------------------------------------------------
%package -n iagno
Summary: Computer version of game Reversi/Othello
Group: Games/Other
Conflicts: gnome-games < 2.29.6-2
Requires: %{name}-common = %{version}-%{release}

%description -n iagno
Iagno is a computer version of the game Reversi, more popularly
called Othello. Iagno is a two player strategy game similar to
Go.  The board is 8 by 8 with tiles that are black on one side
and white on the other side.  The object of Iagno is to flip as
many of your opponent's tiles to your color as possible without
your opponent flipping your tiles.  This is done by trapping your
opponent's tiles between two tiles of your own color.

%files -n iagno -f iagno.lang
%attr(2555, root, games) %{_bindir}/iagno
%{_datadir}/gnome-games/iagno
%{_datadir}/applications/iagno.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.iagno.gschema.xml
%{_iconsdir}/*/*/*/*iagno.*
%{_mandir}/man6/iagno.*

#-----------------------------------------------------------
%package -n lightsoff
Summary: Turn off all the lights
Group: Games/Other
Conflicts: gnome-games < 2.29.6-2
Requires: %{name}-common = %{version}-%{release}
Requires: seed

%description -n lightsoff
Puzzle where all lights have to be switched off.

#files -n lightsoff
#{_sysconfdir}/gconf/schemas/lightsoff.schemas
#attr(2555, root, games) %{_bindir}/lightsoff
#{_datadir}/gnome-games/lightsoff
#{_datadir}/applications/lightsoff.desktop
#{_datadir}/glib-2.0/schemas/org.gnome.lightsoff.gschema.xml
#{_iconsdir}/*/*/*/lightsoff.*

#-----------------------------------------------------------
%package -n gnome-mahjongg
Summary: Mahjongg tile solitaire game
Group: Games/Other
Conflicts: gnome-games < 2.29.6-2
Requires: %{name}-common = %{version}-%{release}

%description -n gnome-mahjongg
A tile-based solitaire game. Remove tiles in matching pairs to
dismantle elaborately designed stacks.

%pre -n gnome-mahjongg
[ -d %{_localstatedir}/games ] || mkdir -p %{_localstatedir}/games
for i in \
  mahjongg.bridges \
  mahjongg.cloud \
  mahjongg.confounding \
  mahjongg.difficult \
  mahjongg.dragon \
  mahjongg.easy \
  mahjongg.pyramid \
  mahjongg.tictactoe \
  mahjongg.ziggurat \
; do
  %create_ghostfile %{_localstatedir}/games/$i.scores games games 0664
  if [ -f "%{_localstatedir}/games/$i.scores" -a ! -s "%{_localstatedir}/games/$i.scores" ]; then
    echo "0.000000 `date +%s` gnome" >> %{_localstatedir}/games/$i.scores
  fi
done

%files -n gnome-mahjongg -f mahjongg.lang
%attr(2555, root, games) %{_bindir}/mahjongg
%{_datadir}/gnome-games/mahjongg
%{_datadir}/applications/mahjongg.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.mahjongg.gschema.xml
%{_iconsdir}/*/*/*/*mahjongg.*
%{_mandir}/man6/mahjongg.*
%attr(664, games, games) %ghost %{_localstatedir}/games/mahjongg.*.scores

#-----------------------------------------------------------
%package -n quadrapassel
Summary: Falling blocks game
Group: Games/Other
Conflicts: gnome-games < 2.29.6-2
Requires: %{name}-common = %{version}-%{release}
Provides: gnometris = %{version}-%{release}

%description -n quadrapassel
The Russian game of falling geometric shapes. Fit blocks together
to make complete rows.

%pre -n quadrapassel
[ -d %{_localstatedir}/games ] || mkdir -p %{_localstatedir}/games
for i in \
  quadrapassel \
; do
  %create_ghostfile %{_localstatedir}/games/$i.scores games games 0664
  if [ -f "%{_localstatedir}/games/$i.scores" -a ! -s "%{_localstatedir}/games/$i.scores" ]; then
    echo "0.000000 `date +%s` gnome" >> %{_localstatedir}/games/$i.scores
  fi
done

%files -n quadrapassel -f quadrapassel.lang
%{_sysconfdir}/gconf/schemas/quadrapassel.schemas
%attr(2555, root, games) %{_bindir}/quadrapassel
%{_datadir}/gnome-games/quadrapassel
%{_datadir}/applications/quadrapassel.desktop
#{_datadir}/glib-2.0/schemas/org.gnome.quadrapassel.gschema.xml
%{_iconsdir}/*/*/*/*quadrapassel.*
%{_mandir}/man6/quadrapassel.*
%attr(664, games, games) %ghost %{_localstatedir}/games/quadrapassel.scores

#-----------------------------------------------------------
%package -n swell-foop
Summary: Colored ball puzzle game
Group: Games/Other
Conflicts: gnome-games < 2.29.6-2
Requires: %{name}-common = %{version}-%{release}
Requires: seed

%description -n swell-foop
Remove blocks of balls of the same color in as few moves as
possible. Try to remove all balls for a bonus.

#files -n swell-foop
#{_sysconfdir}/gconf/schemas/swell-foop.schemas
#attr(2555, root, games) %{_bindir}/swell-foop
#{_datadir}/gnome-games/swell-foop
#{_datadir}/applications/swell-foop.desktop
#{_datadir}/glib-2.0/schemas/org.gnome.swell-foop.gschema.xml
#{_iconsdir}/*/*/*/swell-foop.*

#-----------------------------------------------------------

%package devel
Group: Development/Other
Summary: Gnome games library introspection
Requires: %{name} = %{version}-%{release}

%description devel
This contains GObject-Introspection support for the libraries of %{name}.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--disable-schemas-install \
	--enable-compile-warnings=no

%make

%install
rm -rf %{buildroot}
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std
%find_lang %{name}

%define games glines gnect gnibbles gnobots2 gnome-sudoku gnomine gnotravex gnotski gtali iagno mahjongg glchess quadrapassel 
#lightsoff fswell-foop
for game in %games; do
	%find_lang $game --with-gnome
	sed -i "s|%%lang(sr@latin) %{_datadir}/gnome/help/${game}/sr@latin/figures$||g" ${game}.lang
done

rm -rf %{buildroot}/var/lib/scrollkeeper %{buildroot}%{_sysconfdir}/ggz.modules

%files

%files devel
%{_libdir}/gnome-games/libgames-support-gi.so
%{_libdir}/gnome-games/GnomeGamesSupport-1.0.gir

