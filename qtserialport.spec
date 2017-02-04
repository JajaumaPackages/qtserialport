%global commit 56ebaec
%global snapshot .git20160928.%{commit}

Name:           qtserialport
Version:        5.4.0
Release:        1.beta1%{snapshot}%{?dist}
Summary:        A library providing an interface for serial ports

License:        LGPLv2.1
URL:            https://wiki.qt.io/QtSerialPort

# git clone git://code.qt.io/qt/qtserialport.git
# cd qtserialport
# git checkout qt4-dev
# git archive --prefix=qtserialport/ qt4-dev | bzip2 >../qtserialport.tar.bz2
Source0:        qtserialport.tar.bz2

BuildRequires:  pkgconfig(QtCore)

Provides:       qtserialport-qt4 = %{version}-1%{snapshot}%{?dist}
Provides:       qtserialport-qt4%{?_isa} = %{version}-1%{snapshot}%{?dist}
Obsoletes:      qtserialport-qt4 <= %{version}-1%{snapshot}%{?dist}

%description
Serial interfaces, due to their simplicity and reliability, are still popular
in some industries like the development of embedded systems, robotics, etc.

Using the QtSerialPort module, developers can significantly reduce the time
needed to implement Qt applications that require access to a serial interface.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt4-devel

Provides:       qtserialport-qt4-devel = %{version}-1%{snapshot}%{?dist}
Provides:       qtserialport-qt4-devel%{?_isa} = %{version}-1%{snapshot}%{?dist}
Obsoletes:      qtserialport-qt4-devel <= %{version}-1%{snapshot}%{?dist}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n qtserialport


%build
%{_qt4_qmake}
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install INSTALL_ROOT=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license LGPL_EXCEPTION.txt LICENSE.*
%{_libdir}/*.so.*

%files devel
%doc examples
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.prl
%{_qt4_prefix}/mkspecs/features/*.prf


%changelog
* Sat Feb 04 2017 Jajauma's Packages <jajauma@yandex.ru> - 5.4.0-1.beta1.git20160928.56ebaec
- Rename package to qtserialport and obsolete qtserialport-qt4

* Wed Sep 28 2016 Jajauma's Packages <jajauma@yandex.ru> - 5.4.0-1.git20160928.56ebaec
- Public release
