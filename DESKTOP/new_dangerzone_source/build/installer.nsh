Var SystemDrive

!macro preInit
    ReadEnvStr $SystemDrive SYSTEMDRIVE
    SetRegView 64
    WriteRegExpandStr HKLM "${INSTALL_REGISTRY_KEY}" InstallLocation "$SystemDrive\Program Files\dangerzone"
    WriteRegExpandStr HKCU "${INSTALL_REGISTRY_KEY}" InstallLocation "$SystemDrive\Program Files\dangerzone"
    SetRegView 32
    WriteRegExpandStr HKLM "${INSTALL_REGISTRY_KEY}" InstallLocation "$SystemDrive\Program Files (x86)\dangerzone"
    WriteRegExpandStr HKCU "${INSTALL_REGISTRY_KEY}" InstallLocation "$SystemDrive\Program Files (x86)\dangerzone"
!macroend

!macro customInstall 
    WriteRegStr HKCR "*\shell\OpenwithDangerzone" "" "Open with Dangerzone" 
    WriteRegStr HKCR "*\shell\OpenwithDangerzone\command" "" "$INSTDIR\${APP_EXECUTABLE_FILENAME} %1" 
!macroend