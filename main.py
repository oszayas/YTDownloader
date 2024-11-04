import flet as ft
import os
import yt_dlp
ruta_descarga = os.path.join(os.path.expanduser("~"),"Downloads")
def main(page: ft.Page):
    #Elementos
    stack = ft.Stack()
    etiqueta1 = ft.Text("Descargar videos de Youtube", weight="bold",size=40)
    url_input = ft.TextField(border_color="white",width=500)
    boton_descargar = ft.ElevatedButton(text="Descargar",bgcolor="green",color="white")
    pb = ft.ProgressBar(color="green",width=400,visible=False)


    def descargar(e):
        try:
            pb.visible = True
            url = url_input.value        
            page.update()
            def progesive_hook(d):
                if d['status'] == 'downloading':
                    index = d["fragment_index"]
                    total = d["fragment_count"]
                    percent = (index/total)*100
                    percent = percent*0.01
                    print(percent)
                    pb.value = percent
                    page.update()   

            ydl_opts = {
                    'format': 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=mp4]',
                    'outtmpl':os.path.join(ruta_descarga,'%(title)s.%(ext)s'),     
                    'progress_hooks':[progesive_hook]
                    
                }

                
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                    
            dlg = ft.AlertDialog(title=ft.Text("Completado!"),
                            content=ft.Text("Se descargó el video exitosamente"),
                            actions=[ft.ElevatedButton("Aceptar",on_click=lambda e:page.close(dlg))]
                            )
            page.open(dlg)
            pb.visible=False
            page.update()
        except yt_dlp.utils.DownloadError as e:
            pb.visible=False
            page.update()        
            message = "La url no es valida"
            dlg_error = ft.AlertDialog(title=ft.Text("Error!"),
                            content=ft.Text(value=message),
                            actions=[ft.ElevatedButton("Aceptar",on_click=lambda e:page.close(dlg_error))]
                            )
            
            page.open(dlg_error) 

        except Exception as e: 
            pb.visible=False
            page.update()          
            message = "Ocurrió un error, vuelva a intentarlo\n"+str(e)
            dlg_error = ft.AlertDialog(title=ft.Text("Error!"),
                            content=ft.Text(value=message),
                            actions=[ft.ElevatedButton("Aceptar",on_click=lambda e:page.close(dlg_error))]
                            )
            
            page.open(dlg_error)

   
    #Contenedores
    ce1 = ft.Container(
        content=etiqueta1,
        left=425,
        top=100
    )
    cui = ft.Container(
        content=url_input,
        left=445,
        top=200
    )
    cbd = ft.Container(
        content=boton_descargar,
        left=635,
        top=300
    )
    cpb = ft.Container(
        content=pb,
        left=500,
        top = 400
    )
    
    boton_descargar.on_click = descargar
    stack.controls.append(ce1)
    stack.controls.append(cui)
    stack.controls.append(cbd)
    stack.controls.append(cpb)
    page.window_maximized = True
    page.add(stack)

ft.app(main)