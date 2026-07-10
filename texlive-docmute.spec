%global tl_name docmute
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Input files ignoring LaTeX preamble, etc.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/docmute
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/docmute.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/docmute.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/docmute.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Input or include stand-alone LaTeX documents, ignoring everything but
the material between \begin{document} and \end{document}.

