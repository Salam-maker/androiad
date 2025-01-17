from flet import *
def main(page:Page):
    page.title="FLASH"
    page.scroll="auto"
    page.window.top=1
    page.window.width=390
    page.window.height=740
    page.window.left=960
    page.theme_mode=ThemeMode.SYSTEM
    page.bgcolor="white"
    flash=Flashlight()
    page.overlay.append(flash)

    ph=PermissionHandler()
    page.overlay.append(ph)

    def open_app(e):
        ph.open_app_settings()

    page.add(

        AppBar(
            title=Text('FLASH LIGHT [M.T]'),
            color='white',
            bgcolor='pink',
            actions=[
                IconButton(icons.SETTINGS,on_click=open_app),

            ]
        ),
        Row([
            Text('\n\nFLASH LIGHT APP',size=31,color='black',)
        ],alignment=MainAxisAlignment.CENTER),
        Row([
            Image(src="f.png",width=200,)

        ],alignment=MainAxisAlignment.CENTER),
        Row([
            ElevatedButton(
                'On',
                width=100,
                icon=icons.PLAY_DISABLED_SHARP,
                style=ButtonStyle(
                    bgcolor='pink',
                    color='white',
                    padding=15,
                    shape=ContinuousRectangleBorder(radius=100)
                ),
                on_click=lambda _:flash.turn_on
            ),
            ElevatedButton(
                'Off',
                width=100,
                icon=icons.PLAY_ARROW,
                style=ButtonStyle(
                    bgcolor='pink',
                    color='white',
                    padding=15,
                    shape=ContinuousRectangleBorder(radius=100)
                ),
                on_click=lambda _:flash.turn_off
            )


        ],alignment=MainAxisAlignment.CENTER),
        Row([
            Text('\n\nBY: MOONIGHT.2025 ',size=14,color='black',)
        ],alignment=MainAxisAlignment.CENTER),


    )





    page.update()
app(main)
