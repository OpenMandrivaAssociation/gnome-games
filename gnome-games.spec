Summary:	GNOME games
Name:		gnome-games
Version:	3.6.0
Release:	2
License:	GPLv2+
Group:		Games/Other
URL:		http://live.gnome.org/GnomeGames/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-games/3.6/gnome-games-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	gnome-doc-utils
BuildRequires:	gob2
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	x11-server-xvfb
BuildRequires:	vala
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(clutter-gtk-1.0)
BuildRequires:	pkgconfig(gconf-2.0)
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
Requires:	glchess
Requires:	glines
Requires:	gnect
Requires:	gnibbles
Requires:	gnobots2
Requires:	gnome-mahjongg
Requires:	gnome-sudoku
Requires:	gnomine
Requires:	gnotravex
Requires:	gnotski
Requires:	gtali
Requires:	iagno
Requires:	lightsoff
Requires:	quadrapassel
Requires:	swell-foop

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
Summary:	Common files for GNOME Games
Group:		Games/Other
Conflicts:	gnome-games < 2.29.6-2
Requires:	python-gi-cairo
Requires:	typelib(Gtk) >= 3.0

%description common
Common files for GNOME Games.

%files common -f %{name}.lang

#-----------------------------------------------------------
%package -n glchess
Summary:	Chess with a 3D board
Group:		Games/Other
Conflicts:	gnome-games < 2.29.6-2
Requires:	%{name}-common = %{version}-%{release}

%description -n glchess
Chess with a 3D board.

%files -n glchess -f glchess.lang
%attr(2555, root, games) %{_bindir}/glchess
%{_datadir}/glchess
%{_datadir}/applications/glchess.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.glchess.gschema.xml
%{_iconsdir}/*/*/*/*glchess.*
%{_mandir}/man6/glchess.*

#-----------------------------------------------------------
%package -n glines
Summary:	Move balls
Group:		Games/Other
Conflicts:	gnome-games < 2.29.6-2
Requires:	%{name}-common = %{version}-%{release}

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
%{_datadir}/glines
%{_datadir}/applications/glines.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.glines.gschema.xml
%{_iconsdir}/*/*/*/*glines.*
%{_mandir}/man6/glines.*
%attr(664, games, games) %ghost %{_localstatedir}/games/glines.*.scores

#-----------------------------------------------------------
%package -n gnect
Summary:	A four-in-a-row game
Group:		Games/Other
Conflicts:	gnome-games < 2.29.6-2
Requires:	%{name}-common = %{version}-%{release}

%description -n gnect
gnect is a four-in-a-row game for the GNOME Project.
The object of the game is to build a line of four of your marbles
while trying to stop your opponent (human or computer) building a
line of his or her own. A line can be horizontal, vertical or
diagonal.

%files -n gnect -f gnect.lang
%attr(2555, root, games) %{_bindir}/gnect
%{_datadir}/gnect
%{_datadir}/applications/gnect.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnect.gschema.xml
%{_iconsdir}/*/*/*/*gnect.*
%{_mandir}/man6/gnect.*

#-----------------------------------------------------------
%package -n gnibbles
Summary:	A worm game
Group:		Games/Other
Conflicts:	gnome-games < 2.29.6-2
Requires:	%{name}-common = %{version}-%{release}

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
%attr(2555, root, games) %{_bindir}/gnibbles
%{_datadir}/gnibbles
%{_datadir}/applications/gnibbles.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnibbles.gschema.xml
%{_iconsdir}/*/*/*/*gnibbles.*
%{_mandir}/man6/gnibbles.*
%attr(664, games, games) %ghost %{_localstatedir}/games/gnibbles.*.scores

#-----------------------------------------------------------
%package -n gnobots2
Summary:	Graphical version of text based robots game
Group:		Games/Other
Conflicts:	gnome-games < 2.29.6-2
Requires:	%{name}-common = %{version}-%{release}

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
%attr(2555, root, games) %{_bindir}/gnobots2
%{_datadir}/gnobots2
%{_datadir}/applications/gnobots2.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnobots2.gschema.xml
%{_iconsdir}/*/*/*/gnobots2.*
%{_iconsdir}/hicolor/*/actions/teleport*.png
%{_mandir}/man6/gnobots2.*
%attr(664, games, games) %ghost %{_localstatedir}/games/gnobots2.*.scores

#-----------------------------------------------------------
%package -n gnome-sudoku
Summary:	Generate and play the popular Sudoku logic puzzle
Group:		Games/Other
Conflicts:	gnome-games < 2.29.6-2
Requires:	%{name}-common = %{version}-%{release}

%description -n gnome-sudoku
gnome-sudoku is an application to generate and play the popular
Sudoku logic puzzle (also known as Number Place).

%files -n gnome-sudoku -f gnome-sudoku.lang
%attr(2555, root, games) %{_bindir}/gnome-sudoku
%{py_puresitedir}/gnome_sudoku
%{_datadir}/gnome-sudoku
%{_datadir}/applications/gnome-sudoku.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-sudoku.gschema.xml
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
%{_datadir}/gnomine
%{_datadir}/applications/gnomine.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnomine.gschema.xml
%{_iconsdir}/*/*/*/gnomine.*
%{_mandir}/man6/gnomine.*
%attr(664, games, games) %ghost %{_localstatedir}/games/gnomine.*.scores

#-----------------------------------------------------------
%package -n gnotravex
Summary:	A simple puzzle game
Group:		Games/Other
Conflicts:	gnome-games < 2.29.6-2
Requires:	%{name}-common = %{version}-%{release}

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
%{_datadir}/gnotravex
%{_datadir}/applications/gnotravex.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnotravex.gschema.xml
%{_iconsdir}/*/*/*/gnotravex.*
%{_mandir}/man6/gnotravex.*
%attr(664, games, games) %ghost %{_localstatedir}/games/gnotravex.*.scores

#-----------------------------------------------------------
%package -n gnotski
Summary:	Clone of the Klotski game
Group:		Games/Other
Conflicts:	gnome-games < 2.29.6-2
Requires:	%{name}-common = %{version}-%{release}

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
%attr(2555, root, games) %{_bindir}/gnotski
%{_datadir}/gnotski
%{_datadir}/applications/gnotski.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnotski.gschema.xml
%{_iconsdir}/*/*/*/gnotski.*
%{_mandir}/man6/gnotski.*
%attr(664, games, games) %ghost %{_localstatedir}/games/gnotski.*.scores

#-----------------------------------------------------------
%package -n gtali
Summary:	Tali is like Yahtzee for GNOME
Group:		Games/Other
Conflicts:	gnome-games < 2.29.6-2
Requires:	%{name}-common = %{version}-%{release}

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
%attr(2555, root, games) %{_bindir}/gtali
%{_datadir}/gtali
%{_datadir}/applications/gtali.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gtali.gschema.xml
%{_iconsdir}/*/*/*/*tali.*
%{_mandir}/man6/gtali.*
%attr(664, games, games) %ghost %{_localstatedir}/games/gtali.*.scores

#-----------------------------------------------------------
%package -n iagno
Summary:	Computer version of game Reversi/Othello
Group:		Games/Other
Conflicts:	gnome-games < 2.29.6-2
Requires:	%{name}-common = %{version}-%{release}

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
%{_datadir}/iagno
%{_datadir}/applications/iagno.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.iagno.gschema.xml
%{_iconsdir}/*/*/*/*iagno.*
%{_mandir}/man6/iagno.*

#-----------------------------------------------------------
%package -n lightsoff
Summary:	Turn off all the lights
Group:		Games/Other
Conflicts:	gnome-games < 2.29.6-2
Requires:	%{name}-common = %{version}-%{release}
Requires:	seed

%description -n lightsoff
Puzzle where all lights have to be switched off.

%files -n lightsoff -f lightsoff.lang
%attr(2555, root, games) %{_bindir}/lightsoff
%{_datadir}/lightsoff
%{_datadir}/applications/lightsoff.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.lightsoff.gschema.xml
%{_iconsdir}/*/*/*/lightsoff.*

#-----------------------------------------------------------
%package -n gnome-mahjongg
Summary:	Mahjongg tile solitaire game
Group:		Games/Other
Conflicts:	gnome-games < 2.29.6-2
Requires:	%{name}-common = %{version}-%{release}

%description -n gnome-mahjongg
A tile-based solitaire game. Remove tiles in matching pairs to
dismantle elaborately designed stacks.

%pre -n gnome-mahjongg
[ -d %{_localstatedir}/games ] || mkdir -p %{_localstatedir}/games
for i in \
  gnome-mahjongg.bridges \
  gnome-mahjongg.cloud \
  gnome-mahjongg.confounding \
  gnome-mahjongg.difficult \
  gnome-mahjongg.dragon \
  gnome-mahjongg.easy \
  gnome-mahjongg.pyramid \
  gnome-mahjongg.tictactoe \
  gnome-mahjongg.ziggurat \
; do
  %create_ghostfile %{_localstatedir}/games/$i.scores games games 0664
  if [ -f "%{_localstatedir}/games/$i.scores" -a ! -s "%{_localstatedir}/games/$i.scores" ]; then
    echo "0.000000 `date +%s` gnome" >> %{_localstatedir}/games/$i.scores
  fi
done

%files -n gnome-mahjongg -f gnome-mahjongg.lang
%attr(2555, root, games) %{_bindir}/gnome-mahjongg
%{_datadir}/gnome-mahjongg
%{_datadir}/applications/gnome-mahjongg.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-mahjongg.gschema.xml
%{_iconsdir}/*/*/*/*mahjongg.*
%{_mandir}/man6/gnome-mahjongg.*
%attr(664, games, games) %ghost %{_localstatedir}/games/gnome-mahjongg.*.scores

#-----------------------------------------------------------
%package -n quadrapassel
Summary:	Falling blocks game
Group:		Games/Other
Conflicts:	gnome-games < 2.29.6-2
Requires:	%{name}-common = %{version}-%{release}
Provides:	gnometris = %{version}-%{release}

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
%attr(2555, root, games) %{_bindir}/quadrapassel
%{_datadir}/quadrapassel
%{_datadir}/applications/quadrapassel.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.quadrapassel.gschema.xml
%{_iconsdir}/*/*/*/*quadrapassel.*
%{_mandir}/man6/quadrapassel.*
%attr(664, games, games) %ghost %{_localstatedir}/games/quadrapassel.scores

#-----------------------------------------------------------
%package -n swell-foop
Summary:	Colored ball puzzle game
Group:		Games/Other
Conflicts:	gnome-games < 2.29.6-2
Requires:	%{name}-common = %{version}-%{release}
Requires:	seed

%description -n swell-foop
Remove blocks of balls of the same color in as few moves as
possible. Try to remove all balls for a bonus.

%pre -n swell-foop
[ -d %{_localstatedir}/games ] || mkdir -p %{_localstatedir}/games
for i in \
  swell-foop.large \
  swell-foop.normal \
  swell-foop.small \
; do
  %create_ghostfile %{_localstatedir}/games/$i.scores games games 0664
  if [ -f "%{_localstatedir}/games/$i.scores" -a ! -s "%{_localstatedir}/games/$i.scores" ]; then
    echo "0.000000 `date +%s` gnome" >> %{_localstatedir}/games/$i.scores
  fi
done

%files -n swell-foop -f swell-foop.lang
%attr(2555, root, games) %{_bindir}/swell-foop
%{_datadir}/swell-foop
%{_datadir}/applications/swell-foop.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.swell-foop.gschema.xml
%{_iconsdir}/*/*/*/swell-foop.*
%attr(664, games, games) %ghost %{_localstatedir}/games/swell-foop.*.scores

#-----------------------------------------------------------

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
%makeinstall_std
%find_lang %{name}

%define games glchess glines gnect gnibbles gnobots2 gnome-sudoku gnomine gnotravex gnotski gtali iagno gnome-mahjongg lightsoff quadrapassel swell-foop
for game in %games; do
	%find_lang $game --with-gnome
	#sed -i "s|%%lang(sr@latin) %{_datadir}/help/${game}/sr@latin/figures$||g" ${game}.lang
done

rm -rf %{buildroot}/var/lib/scrollkeeper %{buildroot}%{_sysconfdir}/ggz.modules

%files


%changelog
* Mon Oct  8 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-1
- update to 3.6.0

* Wed May 30 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.4.1-1
+ Revision: 801417
- version update 3.4.1

* Sun Mar 11 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.1-3
+ Revision: 784196
- readded devel pkg
- moved devel libs

* Fri Mar 09 2012 Per Ãyvind Karlsen <peroyvind@mandriva.org> 3.2.1-2
+ Revision: 783462
- rebuild without scriptlet dependencies

* Wed Mar 07 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.1-1
+ Revision: 782606
- added source
- new version 3.2.1
- cleaned up spec
- lightsoff and swell-foop are gone for now
- aisle-riot is a separate pkg
- workaround hack for lang sr@

* Sun May 08 2011 Funda Wang <fwang@mandriva.org> 2.32.1-3
+ Revision: 672420
- add br

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.32.1-2mdv2011.0
+ Revision: 627713
- don't force the usage of automake1.7

* Mon Nov 15 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.1-1mdv2011.0
+ Revision: 597835
- update to new version 2.32.1

  + John Balcaen <mikala@mandriva.org>
    - Fix BR for libcanberra-gtk-devel

* Wed Nov 03 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.0-2mdv2011.0
+ Revision: 592856
- rebuild for python 2.7

* Mon Sep 27 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581207
- update to new version 2.32.0

* Fri Sep 17 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.92.1-1mdv2011.0
+ Revision: 579142
- new version
- drop patch 1
- fix build with external cardsets

* Wed Sep 15 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.92-1mdv2011.0
+ Revision: 578705
- new version
- fix build with new gobject-introspection

* Tue Aug 31 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.91.1-1mdv2011.0
+ Revision: 574574
- update to new version 2.31.91.1

* Mon Aug 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.91-1mdv2011.0
+ Revision: 574288
- update to new version 2.31.91

* Tue Aug 17 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.90-1mdv2011.0
+ Revision: 570832
- update to new version 2.31.90

* Tue Aug 03 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.6-1mdv2011.0
+ Revision: 565412
- update to new version 2.31.6

* Fri Jul 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.5-1mdv2011.0
+ Revision: 563631
- disable check
- new version

* Sun Jul 11 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.2-1mdv2011.0
+ Revision: 550717
- update to new version 2.30.2

* Tue Apr 27 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.1-1mdv2010.1
+ Revision: 539467
- update to new version 2.30.1

* Mon Mar 29 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528918
- new version
- drop patch 1

* Wed Mar 10 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.92-1mdv2010.1
+ Revision: 517351
- new version
- patch to fix build with stable clutter-gtk

* Tue Feb 23 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.91-1mdv2010.1
+ Revision: 510002
- new version
- update file list

* Fri Feb 12 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.6-4mdv2010.1
+ Revision: 504649
- rebuild for new clutter

  + Pascal Terjan <pterjan@mandriva.org>
    - Fix crash of glchess at startup in non UTF-8 locales

* Fri Jan 29 2010 Funda Wang <fwang@mandriva.org> 2.29.6-2mdv2010.1
+ Revision: 497884
- split into several subpackages (as ubuntu)
- linking against math is not needed any more

* Tue Jan 26 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.6-1mdv2010.1
+ Revision: 496512
- new version
- update file list

* Tue Jan 12 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.5-1mdv2010.1
+ Revision: 490123
- new version
- drop extra source file, the tarball was fixed

* Tue Dec 22 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.4-1mdv2010.1
+ Revision: 481284
- add missing file
- new version

* Wed Dec 09 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.3-1mdv2010.1
+ Revision: 475427
- disable make check
- new version
- fix build
- update file list
- update deps

* Thu Oct 22 2009 Frederic Crozat <fcrozat@mandriva.com> 2.28.1-1mdv2010.0
+ Revision: 458835
- Release 2.28.1

* Tue Oct 06 2009 Thierry Vignaud <tv@mandriva.org> 2.28.0-2mdv2010.0
+ Revision: 454724
- do not package huge ChangeLogs

* Mon Sep 21 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446730
- new version
- add man pages

* Thu Sep 10 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.92-1mdv2010.0
+ Revision: 437509
- new version
- fix linking

* Thu Aug 13 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.90-1mdv2010.0
+ Revision: 415961
- new version
- drop patch

* Wed Aug 12 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.5-4mdv2010.0
+ Revision: 415266
- move typelib to the main package

* Thu Jul 30 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.5-3mdv2010.0
+ Revision: 404616
- build with introspection support

* Thu Jul 30 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.5-2mdv2010.0
+ Revision: 404595
- patch for new clutter

* Tue Jul 28 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.5-1mdv2010.0
+ Revision: 401401
- update to new version 2.27.5

* Tue Jul 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.4-1mdv2010.0
+ Revision: 395776
- new version
- update file list

* Tue Jun 16 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.3-1mdv2010.0
+ Revision: 386378
- use xvfb for the checks
- enable unit tests
- new version
- bump clutter deps
- remove old configure option

* Tue May 26 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.2-1mdv2010.0
+ Revision: 379784
- update to new version 2.27.2

* Mon May 11 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.1-1mdv2010.0
+ Revision: 374685
- update build deps
- new version
- bump clutter dep
- update file list

* Tue Apr 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.1-1mdv2009.1
+ Revision: 366921
- update to new version 2.26.1

* Tue Mar 17 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 356490
- update to new version 2.26.0

* Tue Mar 03 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.92-1mdv2009.1
+ Revision: 347631
- update to new version 2.25.92

* Wed Feb 18 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 342355
- new version
- update clutter deps

* Mon Feb 02 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.90-1mdv2009.1
+ Revision: 336678
- update to new version 2.25.90

* Thu Jan 22 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.5-2mdv2009.1
+ Revision: 332528
- enable clutter

* Tue Jan 20 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.5-1mdv2009.1
+ Revision: 331533
- update to new version 2.25.5

* Tue Jan 06 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.4-1mdv2009.1
+ Revision: 325235
- update to new version 2.25.4

* Fri Dec 26 2008 Funda Wang <fwang@mandriva.org> 2.25.3-2mdv2009.1
+ Revision: 319382
- rebuild for new python

* Thu Dec 18 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.3-1mdv2009.1
+ Revision: 315778
- update to new version 2.25.3

* Tue Dec 02 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.2-1mdv2009.1
+ Revision: 309080
- update to new version 2.25.2
- update build deps

* Wed Nov 05 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.1-1mdv2009.1
+ Revision: 299977
- new version
- update file list

* Sun Nov 02 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.1.1-1mdv2009.1
+ Revision: 299289
- update to new version 2.24.1.1

* Tue Oct 21 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 295937
- update to new version 2.24.1

* Mon Sep 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 286438
- new version

* Tue Sep 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.92-1mdv2009.0
+ Revision: 282913
- new version

* Tue Aug 19 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.90-1mdv2009.0
+ Revision: 273624
- new version

* Mon Aug 04 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.6-1mdv2009.0
+ Revision: 263605
- new version

* Mon Jul 21 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.5-1mdv2009.0
+ Revision: 239331
- new version

* Thu Jul 03 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.4-1mdv2009.0
+ Revision: 231095
- new version
- new version
- update file list

* Mon Jun 30 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.3-1mdv2009.0
+ Revision: 230151
- new version
- fix scores dir, it is /var/games now
- update license tag

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Sun Jun 01 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.2.1-1mdv2009.0
+ Revision: 214153
- new version

* Tue May 27 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.2-1mdv2009.0
+ Revision: 211609
- new version
- drop icons

* Tue Apr 15 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.1.1-1mdv2009.0
+ Revision: 193657
- fix buildrequires
- new version
- drop patch
- fix buildrequires

* Tue Mar 25 2008 Frederic Crozat <fcrozat@mandriva.com> 2.22.0-2mdv2008.1
+ Revision: 190006
- Patch0 (SVN): various fixes, including glchess startup on x86-64 (Mdv bug #37463)

* Tue Mar 11 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 185041
- new version

* Tue Feb 26 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.92-1mdv2008.1
+ Revision: 175282
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - fix gstreamer0.10-devel BR for x86_64

* Tue Feb 12 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.91-1mdv2008.1
+ Revision: 165767
- new version

* Tue Jan 29 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.90-1mdv2008.1
+ Revision: 159677
- new version
- update file list

* Tue Jan 15 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.5-1mdv2008.1
+ Revision: 152139
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.4-1mdv2008.1
+ Revision: 129350
- fix buildrequires
- new version
- update file list

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 10 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.3-2mdv2008.1
+ Revision: 116932
- resolve conflict with ggz-client-libs (bug #35956)
- regenerate ggz.modules in postinstall script

* Tue Dec 04 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.3-1mdv2008.1
+ Revision: 115277
- fix buildrequires
- new version
- update file list

* Wed Nov 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.2-1mdv2008.1
+ Revision: 108687
- new version

* Tue Oct 30 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.1-1mdv2008.1
+ Revision: 103740
- new version

* Tue Oct 16 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.1-1mdv2008.1
+ Revision: 98887
- new version

* Tue Sep 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.0.1-1mdv2008.0
+ Revision: 89751
- new version
- new version

* Wed Sep 05 2007 Frederic Crozat <fcrozat@mandriva.com> 2.19.92-2mdv2008.0
+ Revision: 79782
- Remove old menu file
- Remove obsolete categories

* Mon Sep 03 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.92-1mdv2008.0
+ Revision: 78805
- new version

* Tue Aug 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.91.1-1mdv2008.0
+ Revision: 72889
- new version

* Tue Aug 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.91-1mdv2008.0
+ Revision: 72378
- new version

* Wed Aug 15 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.90.1-1mdv2008.0
+ Revision: 63638
- new version

* Tue Aug 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.90-1mdv2008.0
+ Revision: 62968
- new version

* Sat Jul 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.6-1mdv2008.0
+ Revision: 56460
- new version

* Mon Jun 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.4-1mdv2008.0
+ Revision: 41114
- new version
- fix desktop file
- new version
- update file list
- fix buildrequires

  + Anssi Hannula <anssi@mandriva.org>
    - rebuild with correct optflags

* Wed May 30 2007 Frederic Crozat <fcrozat@mandriva.com> 2.18.2-2mdv2008.0
+ Revision: 32864
- Fix missing score files (Mdv bug #29338)
- no longer remove Applications category, it is already done upstream

* Mon May 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.2-1mdv2008.0
+ Revision: 32120
- new version

* Sun May 06 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.1.1-1mdv2008.0
+ Revision: 23688
- new version

* Tue Apr 17 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.1-1mdv2008.0
+ Revision: 14116
- new version


* Tue Mar 20 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.0.1-1mdv2007.1
+ Revision: 147128
- new version
- update file list

* Mon Mar 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 142127
- new version

* Tue Feb 27 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.92-1mdv2007.1
+ Revision: 126214
- new version

* Wed Feb 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.91-1mdv2007.1
+ Revision: 120786
- fix buildrequires
- new version

* Wed Jan 24 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.90.1-1mdv2007.1
+ Revision: 112733
- new version
- drop patch

* Tue Jan 23 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.90-2mdv2007.1
+ Revision: 112486
- patch to fix glchess crash on startup (bug #28366)

* Mon Jan 22 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.90-1mdv2007.1
+ Revision: 111740
- new version
- obsolete glchess

* Mon Jan 08 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.5-1mdv2007.1
+ Revision: 105464
- fix buildrequires
- new version
- add new files

* Sun Jan 07 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.4.1-2mdv2007.1
+ Revision: 105288
- rebuild for guile

* Wed Dec 20 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.4.1-1mdv2007.1
+ Revision: 100372
- new version
- drop patch

* Tue Dec 19 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.4-1mdv2007.1
+ Revision: 99116
- new version
- patch to add missing files
- update file list

* Thu Dec 07 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.3-4mdv2007.1
+ Revision: 91932
- add missing deps
- update description

* Wed Dec 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.3-3mdv2007.1
+ Revision: 91659
- bot rebuild
- bot rebuild
- new version

* Tue Nov 28 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.2-3mdv2007.1
+ Revision: 87918
- bot rebuild
- fix buildrequires for broken x86_64 arch
- new version
- add new games
- remove gataxx
- update deps

* Wed Nov 22 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.2-1mdv2007.1
+ Revision: 86182
- new version

* Wed Nov 08 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.1.1-1mdv2007.1
+ Revision: 78047
- new version
- Import gnome-games

* Fri Oct 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.1-1mdv2007.0
- New version 2.16.1

* Wed Sep 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.0-1mdv2007.0
- New release 2.16.0

* Wed Aug 23 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.92-1mdv2007.0
- New release 2.15.92

* Wed Aug 09 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.6-1mdv2007.0
- New release 2.15.6

* Fri Aug 04 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.5-2mdv2007.0
- Rebuild with latest dbus

* Wed Jul 26 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.5-1
- New release 2.15.5

* Wed Jul 12 2006 Götz Waschk <waschk@mandriva.org> 2.15.4-1mdv2007.0
- new macros
- xdg menu
- New release 2.15.4

* Tue Jun 13 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.3-1
- New release 2.15.3

* Fri Jun 09 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.2-2mdv2007.0
- Rebuild

* Sat Jun 03 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.2-1mdv2007.0
- Release 2.15.2

* Tue May 30 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.2-1mdv2007.0
- New release 2.14.2

* Thu Apr 20 2006 Frederic Crozat <fcrozat@mandriva.com> 2.14.1-1mdk
- Release 2.14.1
- Patch0 (CVS): fix broken po

* Wed Mar 08 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.3-2mdk
- rebuild for new libgsf

* Mon Feb 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.3-1mdk
- New release 2.12.3
- use mkrel

* Mon Nov 28 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.2-1mdk
- New release 2.12.2

* Wed Oct 12 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.1-2mdk
- rebuild for new libgsf

* Sat Oct 08 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-1mdk
- Release 2.12.1

* Tue Jul 19 2005 Götz Waschk <waschk@mandriva.org> 2.10.2-1mdk
- New release 2.10.2

* Fri May 06 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.10.1-3mdk
- add BuildRequires: gnome-common intltool

* Wed May 04 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-2mdk 
- Fix url
- Fix build on x86-64

* Thu Apr 21 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-1mdk 
- Release 2.10.1 (based on Götz Waschk package)

* Tue Mar 08 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.3-2mdk 
- Requires svg gdk-pixbuf loader (Mdk bug #14373)

* Mon Feb 14 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 2.8.3-1mdk
- New release 2.8.3

* Thu Jan 06 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.2-2mdk 
- Rebuild with latest howl

* Thu Dec 02 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.8.2-1mdk
- New release 2.8.2

* Thu Nov 11 2004 Götz Waschk <waschk@linux-mandrake.com> 2.8.1-2mdk
- score files (Abel Cheung)

* Wed Nov 10 2004 Götz Waschk <waschk@linux-mandrake.com> 2.8.1-1mdk
- fix omf listing
- drop library package
- New release 2.8.1

* Tue Nov 02 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.6.2-4mdk
- 64-bit fixes

* Sat Aug 21 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.2-3mdk
- Patch0 : fix typo in pa.po, causing gconf warning

* Tue Aug 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 2.6.2-2mdk
- Rebuild with new menu

* Thu Jun 24 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.2-1mdk
- reenable libtoolize
- New release 2.6.2

* Sat Jun 05 2004 <lmontel@n2.mandrakesoft.com> 2.6.1-4mdk
- Rebuild

* Tue Apr 27 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.1-3mdk
- fix buildrequires

* Fri Apr 23 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.1-2mdk
- fix buildrequires

* Wed Apr 21 2004 Goetz Waschk <goetz@mandrakesoft.com> 2.6.1-1mdk
- New release 2.6.1

* Thu Apr 08 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.0.1-1mdk
- Release 2.6.0.1 (with Götz help)
- remove patch0 (merged upstream)

