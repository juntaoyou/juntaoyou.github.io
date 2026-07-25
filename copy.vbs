Set fso = CreateObject("Scripting.FileSystemObject")
src = "D:\Homepage\juntaoyou.github.io\_pages\主页照.jpg"
dst_dir = "D:\Homepage\juntaoyou.github.io\images"
dst = dst_dir & "\profile.jpg"

If fso.FileExists(src) Then
    If Not fso.FolderExists(dst_dir) Then
        fso.CreateFolder(dst_dir)
    End If
    fso.CopyFile src, dst, True
    WScript.Echo "Copied successfully"
Else
    WScript.Echo "Source not found"
End If
