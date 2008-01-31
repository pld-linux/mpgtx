
# NOTE: it won't build with -O3

Summary:	MPeG ToolboX
Summary(pl.UTF-8):	MPeG ToolboX - narzędzia do plików MPEG
Name:		mpgtx
Version:	1.3.1
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/mpgtx/%{name}-%{version}.tar.gz
# Source0-md5:	d628060aa04ad3b40a175bf35f5167cf
URL:		http://mpgtx.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mpgtx allows you to split, join, demultiplex, manipulate ID3 tags and
fetch detailed information about a variety of MPEG files. mpgtx was
designed with the good old Unix philosophy in mind: 'do little, but do
it well, and provide the end user with an austere yet powerful
command line interface.'

%description -l pl.UTF-8
mpgtx umożliwia dzielenie, łączenie, usuwanie przeplotu, modyfikowanie
znaczników ID3 oraz pobieranie szczegółowych informacji o różnych
plikach MPEG. mpgtx został zaprojektowany zgodnie ze starą dobrą
uniksową filozofią: "rób mało, ale rób to dobrze i udostępnij
użytkownikowi prosty, ale potężny interfejs linii poleceń".

%prep
%setup -q

%build
./configure \
	%{?with_debug:--parachute --devel}
%{__make} \
	CFLAGS="%{rpmcflags} -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -DNOSIGNAL_H"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_exec_prefix} \
	manprefix=$RPM_BUILD_ROOT%{_prefix}/share

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/mpg[!t]*
for f in mpgcat mpgdemux mpginfo mpgjoin mpgsplit; do
	echo '.so mpgtx.1' > $RPM_BUILD_ROOT%{_mandir}/man1/${f}.1
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
