Name:           rlwrap
Version:        0.35
Release:        %mkrel 1
Epoch:          0
Summary:        Readline wrapper
Group:          Text tools
License:        GPL
URL:            http://utopia.knoware.nl/~hlub/rlwrap/
Source0:        http://utopia.knoware.nl/~hlub/rlwrap/rlwrap-%{version}.tar.gz
BuildRequires:  libncurses-devel
BuildRequires:  libreadline-devel
BuildRoot:      %{_tmppath}/%{name}-%{epoch}:%{version}-%{release}-root

%description
rlwrap is a 'readline wrapper' that uses the GNU readline library to
allow the editing of keyboard input for any other command. Input
history is remembered across invocations, separately for each command;
history completion and search work as in bash and completion word
lists can be specified on the command line.

%prep
%setup -q

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%check
%{make} check

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc AUTHORS BUGS COPYING ChangeLog INSTALL NEWS README TODO PLEA
%attr(0755,root,root) %{_bindir}/rlwrap
%{_mandir}/man1/rlwrap.1*
%{_mandir}/man3/RlwrapFilter.3pm*
%dir %{_datadir}/rlwrap
%{_datadir}/rlwrap/*
