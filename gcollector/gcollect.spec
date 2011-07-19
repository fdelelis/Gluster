Name:           gcollect
Version:        0.1
Release:        1%{?dist}
Summary:        Simplifying the monitoring of the Gluster distributed filesystem

Group:          Applications/System
License:        GPLv3
URL:            https://github.com/Gestas/Gluster/tree/master/gcollector
Source0:        %{name}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  
#Requires:       

%description
Gcollector is a program designed to make monitoring of the Gluster distributed filesystem as painless
as possible. It was written to run and consolidate the output of many different programs
needed to monitor the health and I/O statistics of Gluster file system volumes, but 
should be useful for many other cases.


%prep
%setup -q -c


%build


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc LICENCE README
/etc/gcollect/*.d/distribute
/etc/gcollect/*.d/distributed-replicate
/etc/gcollect/*.d/replicate
%config(noreplace) /etc/gcollect/gcollect.cfg
%attr(0755,-,-) /usr/sbin/gcollect
%attr(0755,-,-) /usr/sbin/niopid



%changelog
* Tue Jul 19 2011 Greg Swift <gregswift@gmail.com> - 0.1-1
- Initial build
