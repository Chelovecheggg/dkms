Summary:	Dynamic Kernel Module Support
Summary(pl):	Obs�uga dynamicznych modu��w j�dra
Name:		dkms
Version:	2.0.11
Release:	0.1
License:	GPL
Group:		Base/Kernel
Source0:	http://linux.dell.com/dkms/%{name}-%{version}.tar.gz
# Source0-md5:	6eff10dd54fe1a5fde4f3abafb50606b
URL:		http://linux.dell.com/projects.shtml#dkms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var/lib/%{name}
%define		_sysconfdir	/etc/%{name}

%description
DKMS stands for Dynamic Kernel Module Support. It is designed to
create a framework where kernel dependant module source can reside so
that it is very easy to rebuild modules as you upgrade kernels. This
will allow Linux vendors to provide driver drops without having to
wait for new kernel releases while also taking out the guesswork for
customers attempting to recompile modules for new kernels.

%description -l pl
DKMS (Dynamic Kernel Module Support) to obs�uga dynamicznych modu��w
j�dra. Zosta�a zaprojektowana aby stworzy� szkielet do przechowywania
�r�de� modu��w zale�nych od j�dra w spos�b �atwy do zbudowania modu��w
po uaktualnieniu j�dra. Pozwala to dostawcom Linuksa udost�pnia�
sterowniki bez czekania na nowe wydania j�dra ani rozwi�zywania
problem�w klient�w pr�buj�cych przebudowa� modu�y dla nowych j�der.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_sysconfdir},%{_mandir}/man8,%{_localstatedir},/etc/rc.d/init.d}
install dkms $RPM_BUILD_ROOT%{_sbindir}
install dkms.8 $RPM_BUILD_ROOT%{_mandir}/man8
install dkms_dbversion $RPM_BUILD_ROOT%{_localstatedir}
install dkms_autoinstaller $RPM_BUILD_ROOT/etc/rc.d/init.d
install dkms_mkkerneldoth $RPM_BUILD_ROOT%{_sbindir}
install dkms_framework.conf $RPM_BUILD_ROOT%{_sysconfdir}/framework.conf
install template-dkms-mkrpm.spec $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS sample.spec
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/framework.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/template-dkms-mkrpm.spec
%attr(754,root,root) /etc/rc.d/init.d/dkms_autoinstaller
%attr(755,root,root) %{_sbindir}/dkms
%attr(755,root,root) %{_sbindir}/dkms_mkkerneldoth
%{_mandir}/man?/*
%{_localstatedir}
