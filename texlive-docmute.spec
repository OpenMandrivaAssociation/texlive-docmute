# revision 17851
# category Package
# catalog-ctan /macros/latex/contrib/docmute
# catalog-date 2010-04-12 18:27:30 +0200
# catalog-license lppl1.3
# catalog-version 1.2
Name:		texlive-docmute
Version:	1.2
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Input or include stand-alone LaTeX documents, ignoring
everything but the material between \begin{document} and
\end{document}.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/docmute/docmute.sty
%doc %{_texmfdistdir}/doc/latex/docmute/README
%doc %{_texmfdistdir}/doc/latex/docmute/docmute.pdf
#- source
%doc %{_texmfdistdir}/source/latex/docmute/docmute.dtx
%doc %{_texmfdistdir}/source/latex/docmute/docmute.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
