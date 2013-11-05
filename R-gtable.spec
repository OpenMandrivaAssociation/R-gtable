%global packname  gtable
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.1.2
Release:          1
Summary:          Arrange grobs in tables
Group:            Sciences/Mathematics
License:          GPLv2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core

Requires:         R-grid

Requires:         R-testthat R-plyr 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-grid

BuildRequires:   R-testthat R-plyr 
%description
Tools to make it easier to work with "tables" of grobs.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/tests
