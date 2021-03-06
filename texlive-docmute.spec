# revision 25741
# category Package
# catalog-ctan /macros/latex/contrib/docmute
# catalog-date 2012-03-22 16:41:56 +0100
# catalog-license lppl1.3
# catalog-version 1.4
Name:		texlive-docmute
Version:	1.4
Release:	10
Summary:	Input files ignoring LaTeX preamble, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/docmute
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docmute.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docmute.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docmute.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Input or include stand-alone LaTeX documents, ignoring
everything but the material between \begin{document} and
\end{document}.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/docmute/docmute.sty
%doc %{_texmfdistdir}/doc/latex/docmute/README
%doc %{_texmfdistdir}/doc/latex/docmute/docmute.pdf
#- source
%doc %{_texmfdistdir}/source/latex/docmute/docmute.dtx
%doc %{_texmfdistdir}/source/latex/docmute/docmute.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.4-1
+ Revision: 787579
- Update to latest release.

* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 770139
- Update to latest upstream package

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 751007
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 718244
- texlive-docmute
- texlive-docmute
- texlive-docmute
- texlive-docmute

