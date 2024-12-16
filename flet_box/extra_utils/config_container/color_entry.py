import flet as ft


class ColorEntry(ft.Stack):
    """
    box_layout = ft.Container(content=ft.Text())

    Double_Widget = DoubleEntry
    Double_Widget(config_widget='value',widget = box_layout),
    """

    def __init__(
        self,
        page: object = None,
        id_name_widget_dict=None,
        screen_phone: object = None,
        config_widget: str = "exemple [value,bgcolor,width,height] ....",
    ):
        super().__init__()
        self.page = page
        self.widget = screen_phone

        self.tmp_widget_name = " Open"
        self.tooltip = "ColorEntry"
        self.widget_name = config_widget
        self.id_name_widget_dict = id_name_widget_dict

    def build(self):
        ColorEntry = ft.Container(
            ink=False,
            bgcolor="#0c0d0e",
            padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
            margin=ft.margin.all(0),
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(16),
            border=ft.border.all(2, ft.colors('black')),
            width=165,
            height=80,
            content=ft.Column(
                wrap=True,
                controls=[
                    ft.Container(
                        ink=False,
                        bgcolor="#0e0f11",
                        padding=ft.padding.only(
                            left=8, top=0, right=8, bottom=0),
                        alignment=ft.alignment.center,
                        border_radius=ft.border_radius.all(30),
                        height=20,
                        content=ft.Text(
                            value=self.widget_name.capitalize().replace("_", " "),
                            font_family="Consolas",  # "Consolas ,RobotoSlab
                        ),
                    ),
                    ft.Container(
                        ink=False,
                        padding=ft.padding.only(
                                            left=2,
                                            top=0,
                                            right=8,
                                            bottom=0
                        ),
                        alignment=ft.alignment.center,
                        border_radius=ft.border_radius.all(30),
                        border=ft.border.all(1, ft.colors('black38')),
                        width=152,
                        height=36,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[
                                ft.colors('cyan800'),
                                ft.colors('black38'),
                            ],
                        ),
                        content=ft.Row(
                            spacing=4.5,
                            controls=[
                                ft.Container(
                                    ink=False,
                                    bgcolor="#44CCCC00",
                                    width=90,
                                    height=30,
                                    border_radius=ft.border_radius.all(30),
                                    gradient=ft.LinearGradient(
                                        begin=ft.alignment.top_center,
                                        end=ft.alignment.center_right,
                                        colors=[
                                            ft.colors('black12'),
                                            ft.colors('cyan900'),
                                            ft.colors('black38'),
                                        ],
                                    ),
                                    content=ft.ElevatedButton(
                                        text=self.tmp_widget_name,
                                        bgcolor=ft.colors('transparent'),
                                        # ======================= EVENTS ===========================
                                        on_click=lambda _: self.validate_click(
                                                                widget_name=self.widget_name,
                                                                attribute_to_change=self.widget,
                                        ),
                                    ),
                                ),
                                ft.Container(
                                    ink=False,
                                    bgcolor=ft.colors('transparent'),
                                    width=50.5,
                                    height=30,
                                    border=ft.border.all(
                                                    1,
                                                    ft.colors('cyan800')
                                    ),
                                    border_radius=ft.border_radius.all(30),
                                    on_click=lambda x: self.modify_right_container_attributes(
                                                                data=self.widget_name,
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )
        return ColorEntry

    def validate_click(self, widget_name, attribute_to_change):
        #: ONLY PURPOSE IS HIDE CONFIG TO SHOW PALETTE COLORS AND IMAGEN
        print("[+] change content tab [ color_entry.py ]")

        self.tab_container = self.page.session.get('PHOTO_SELECTION')

        self.tab_container.controls[0].visible = False
        self.tab_container.controls[1].visible = False
        self.tab_container.controls[2].visible = True
        self.tab_container.update()

        self.page.session.set('set_attribute_color', widget_name)
        self.page.session.set('set_edit_widget_color', attribute_to_change)

        self.page.update()

    def modify_right_container_attributes(self, data: str=str()):  #: RIGHT BUTTON
        #: ONLY FOR CONTAINER
        if data == "bgcolor":
            self.widget.bgcolor = ft.colors('transparent')

        if data == "focused_bgcolor":
            self.widget.focused_bgcolor = ft.colors('transparent')

        if data == "color":
            self.widget.color = ft.colors('transparent')

        if data == "fill_color":
            self.widget.fill_color = ft.colors('transparent')

        if data == "icon_color":
            self.widget.icon_color = ft.colors('transparent')

        if data == "check_color":
            self.widget.check_color = ft.colors('transparent')

        if data == "focused_border_color":
            self.widget.focused_border_color = ft.colors('transparent')

        if data == "border_color":
            self.widget.border_color = ft.colors('transparent')

        if data == "shadow_color":
            self.widget.shadow = ft.BoxShadow(
                spread_radius=0,
                blur_radius=24,
                color=ft.colors('transparent'),
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,  # NORMAL # SOLID # OUTER # INNER
            )
        self.widget.update()
