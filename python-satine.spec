%define		module	satine
%define		_beta	beta-1
Summary:	Satine - XML data binding for Python
Summary(pl.UTF-8):	Satine - obsługa danych XML dla Pythona
Name:		python-%{module}
Version:	1.0
Release:	0.beta1.4
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/satine/Satine-%{version}_%{_beta}.zip
# Source0-md5:	18a153cc9ed3cd45416d8461911029a2
URL:		http://satine.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	unzip
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Satine is a Python library that makes XML management easy and
complete. Satine converts XML documents to Python lists with
attributes (xlist). This technology allows to:
- translate documents with namespaces, both in elements and attributes
- translate both documents without XMLSchema and documents with it. If
  the XMLSchema is available, the document can be easily validated.
- random and partial access to XML documents
- work very fast. The data binding technology is coded in C.

%description -l pl.UTF-8
Satine to biblioteka Pythona czyniąca zarządzanie XML-em łatwym i
pełnym. Satine konwertuje dokumenty XML na pythonowe listy z
atrybutami (xlist). Technologia ta pozwala na:
- tłumaczenie dokumentów z przestrzeniami nazw, zarówno w elementach
  jak i atrybutach
- tłumaczenie dokumentów zarówno bez XMLSchema jak i z. Jeśli
  XMLSchema jest dostępny, dokument może być łatwo sprawdzony pod
  kątem poprawności.
- swobodny i częściowy dostęp do dokumentów XML
- bardzo szybkie działanie. Technologia obsługi danych jest
  oprogramowana w C.

%prep
%setup -q -n Satine-%{version}_%{_beta}

%build
#python config_unix.py \
#	--prefix %{_prefix}
python setup.py config
%py_build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}

%py_install \
	--root $RPM_BUILD_ROOT

mv examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGE doc/*
%dir %{py_sitedir}/%{module}
%attr(755,root,root) %{py_sitedir}/satine/*.so
%{py_sitedir}/%{module}/*.py[co]
%dir %{py_sitedir}/%{module}/test
%{py_sitedir}/%{module}/test/*.py[co]
%dir %{py_sitedir}/%{module}/schemas
%{py_sitedir}/%{module}/schemas/*.py[co]
%dir %{py_sitedir}/%{module}/grapes
%{py_sitedir}/%{module}/grapes/*.py[co]
%dir %{_examplesdir}/%{name}
%{_examplesdir}/%{name}/*
