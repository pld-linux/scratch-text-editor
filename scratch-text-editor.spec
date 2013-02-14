Summary:	Text editor written in Vala
Name:		scratch-text-editor
Version:	1.1.1
Release:	0.1
License:	GPL v3
Group:		X11/Applications/Editors
#Source0:	https://launchpad.net/scratch/1.x/1.1.1/+download/scratch-%{version}.tar.gz
Source0:	scratch-%{version}-r991.tar.bz2
# Source0-md5:	65d6df04f254562f2be71561e2adae05
# https://bugs.launchpad.net/scratch/+bug/1051678
URL:		https://launchpad.net/scratch/
BuildRequires:	GConf2-devel
BuildRequires:	cmake
BuildRequires:	devhelp-devel
BuildRequires:	gail-devel
BuildRequires:	gobject-introspection
BuildRequires:	granite-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-webkit3-devel
BuildRequires:	gtksourceview-devel
BuildRequires:	gtkspell3-devel
BuildRequires:	libgee0.6-devel
BuildRequires:	libpeas-devel
BuildRequires:	libsoup-devel
BuildRequires:	libsoup-gnome-devel
BuildRequires:	libzeitgeist-devel
#BuildRequires:	pantheon-files
BuildRequires:	pkg-config
BuildRequires:	python-chardet
BuildRequires:	rpmbuild(macros) >= 1.228
BuildRequires:	sed >= 4.0
BuildRequires:	vala
BuildRequires:	vte0-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scratch is the text editor that works for you. It auto-saves your
files, meaning they're always up-to-date. Plus it remembers your tabs
so you never lose your spot, even in between sessions.

Make it yours. Scratch is written from the ground up to be extensible.
Keep things super lightweight and simple, or install extensions to
turn Scratch into a full-blown IDE; it's your choice. And with a
handful of useful preferences, you can tweak the behavior and
interface to your liking.

It's elementary. Scratch is made to be the perfect text editor for
elementary, meaning it closely follows the high standards of design,
speed, and consistency. It's sexy, but not distracting.

Works with your language. Whether you're crafting code in Vala,
scripting with PHP, or marking things up in HTML, Scratch has you
covered. Experience full syntax highlighting with nearly all
programming, scripting, and markup languages.

Other syntax-highlighted languages: Bash, C, C#, C++. Cmake, CSS,
.desktop, Diff, Fortran, Gettext, ini, Java, JavaScript, LaTex, Lua,
Makefile, Objective C, Pascal, Perl, Python, Ruby, XML.

%prep
%setup -q -n scratch

%{__sed} -i -e 's/gtkspell-3.0/gtkspell3-3.0/' plugins/spell-check/CMakeLists.txt

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install -C build \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS CHANGES ChangeLog NEWS README THANKS TODO
