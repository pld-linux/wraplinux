Summary:	Utility to wrap a Linux kernel and initrd into an ELF or NBI file
Summary(pl.UTF-8):	Narzędzie do obudowywania jądra Linuksa wraz z initrd w plik ELF lub NBI
Name:		wraplinux
Version:	1.7
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/System
Source0:	ftp://ftp.kernel.org/pub/linux/utils/boot/wraplinux/%{name}-%{version}.tar.bz2
# Source0-md5:	bd53eaf1172f894d3d3569291bffaf1b
URL:		http://freshmeat.net/projects/wraplinux/
%ifarch %{x8664}
# not exactly multilib as x86 libs are not needed, but gcc with -m32 support
BuildRequires:	gcc-multilib
%endif
# building utility (to work on Linux x86 images) requires x86 crosscompiler
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tool to wrap an x86 Linux kernel and one or more initrd files into a
single file in ELF or NBI format, as required by some booting
protocols (such as Etherboot/Netboot). It can be considered a
replacement for the mknbi and mkelf utilities.

%description -l pl.UTF-8
Narzędzie do obudowywania jądra Linuksa x86 wraz z jednym lub większą
liczbą plików initrd w pojedynczy plik w formacie ELF lub NBI,
wymagany przez niektóre protokołu startowe (jak Etherboot/Netboot).
Może być uznane za zamiennik narzędzi mknbi i mkelf.

%prep
%setup -q

%build
%configure
%{__make} \
%ifarch %{ix86} %{x8664}
	CC_FOR_TARGET="%{__cc} -m32"
%else
	CC_FOR_TARGET="i386-pld-linux-gcc -m32"
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALLROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wraplinux
%{_mandir}/man1/wraplinux.1*
