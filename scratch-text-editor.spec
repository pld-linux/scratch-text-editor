Summary:	Text editor written in Vala
Name:		scratch-text-editor
Version:	1.1.1
Release:	0.1
License:	GPL v3
Group:		X11/Applications/Editors
Source0:	https://launchpad.net/scratch/1.x/1.1.1/+download/scratch-%{version}.tar.gz
# Source0-md5:	c82784fcd53641b6436109eee009dcde
URL:		https://launchpad.net/scratch/
BuildRequires:	GConf2-devel
BuildRequires:	cmake
BuildRequires:	devhelp-devel < 3.6
BuildRequires:	gail-devel
BuildRequires:	gobject-introspection
BuildRequires:	granite-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-webkit3-devel
BuildRequires:	gtksourceview-devel
BuildRequires:	gtkspell-devel
BuildRequires:	libgee0.6-devel
BuildRequires:	libpeas-devel
BuildRequires:	libsoup-devel
BuildRequires:	libsoup-gnome-devel
BuildRequires:	libzeitgeist-devel
#BuildRequires:	pantheon-files
BuildRequires:	pkg-config
BuildRequires:	python-chardet
BuildRequires:	rpmbuild(macros) >= 1.228
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
