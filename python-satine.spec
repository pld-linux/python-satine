%define		module	satine
%define		_beta	beta-1
Summary:	Satine - XML data binding for Python
Summary(pl):	Satine - obs³uga danych XML dla Pythona
Name:		python-%{module}
Version:	1.0
Release:	0.beta.3
License:	GPL
Group:		Libraries/Python
# Source0-md5:	18a153cc9ed3cd45416d8461911029a2
Source0:	http://dl.sourceforge.net/satine/Satine-%{version}_%{_beta}.zip
URL:		http://satine.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
Requires:	python-modules
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

%description -l pl
Satine to biblioteka Pythona czyni±ca zarz±dzanie XML-em ³atwym i
pe³nym. Satine konwertuje dokumenty XML na pythonowe listy z
atrybutami (xlist). Technologia ta pozwala na:
- t³umaczenie dokumentów z przestrzeniami nazw, zarówno w elementach
  jak i atrybutach
- t³umaczenie dokumentów zarówno bez XMLSchema jak i z. Je¶li
  XMLSchema jest dostêpny, dokument mo¿e byæ ³atwo sprawdzony pod
  k±tem poprawno¶ci.
- swobodny i czê¶ciowy dostêp do dokumentów XML
- bardzo szybkie dzia³anie. Technologia obs³ugi danych jest
  oprogramowana w C.

%prep
%setup -q -n Satine-%{version}_%{_beta}

%build
#python config_unix.py \
#	--prefix %{_prefix}
python setup.py config
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}

python setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

mv examples $RPM_BUILD_ROOT%{_examplesdir}/%name
	
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
%dir %{_examplesdir}/%name
%{_examplesdir}/%name/*
