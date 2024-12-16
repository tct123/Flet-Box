import flet as ft

from .double_entry import DoubleEntry
from .color_entry import ColorEntry
from .bool_entry import BoolEntry
from .four_entry import FourEntry
from .single_entry import SingleEntry
from .gradient_entry import GradientEntry
from .blur_color_entry import BlurColorEntry
from .selection_entry import SelectionEntry
from .selection_button_entry import SelectionButtonEntry
from .single_number_entry import SingleNumeberEntry
from .dual_number_entry import DualNumeberEntry


# from ..settings_var.settings_widget import GLOBAL_VAR
from .photo_selection import ScreenPhotoSelection
from .small_palette_color import Screen_palette


class BoxConfigContainer(ft.Container):
    def __init__(self,
                 title: str = "",
                 size_screen: float = float(),
                 controls: list = [],
                 ):
        super().__init__()

        self.tooltip = "BoxConfigContainer"
        self.title = title
        self.controls = controls
        # self.bgcolor = ft.colors('black26')
        # self.size=0.01
        self.padding = ft.padding.only(
            left=0,
            top=0,
            right=0,
            bottom=0)
        self.margin = ft.margin.only(left=0, top=0, right=0, bottom=0)
        # self.scale = 0.8
        self.selection_size_page = size_screen
        # self.alignment = ft.alignment.center

    def build(self):
        # Drop_BoxConfigContainer = ft.Container(
        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            # wrap=True,
            controls=[
                ft.Container(
                    border_radius=ft.border_radius.all(20),
                    bgcolor=ft.colors('black26'),
                    padding=ft.padding.only(
                        left=8,
                        top=2,
                        right=8,
                        bottom=2),
                    margin=ft.margin.only(
                        left=8,
                        top=2,
                        right=20,
                        bottom=2),
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[
                            ft.colors('teal'),
                            ft.colors('black38')
                        ],),
                    content=ft.Text(
                        value=self.title,
                        text_align=ft.TextAlign.CENTER,
                        font_family="Consolas",  # "Consolas ,RobotoSlab
                        color=ft.colors('white'),
                    ),
                ),
                ft.Container(
                    bgcolor=ft.colors('black38'),
                    # expand=True,
                    # bgcolor="red",
                    width=self.selection_size_page,
                    # width=270,
                    # width=425,
                    padding=ft.padding.only(
                        left=2,
                        top=2,
                        right=2,
                        bottom=2),
                    border_radius=ft.border_radius.all(20),
                    content=ft.Row(
                        # scroll=True,
                        # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        # vertical       START,CENTER END
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,

                        wrap=True,
                        controls=self.controls,),),
            ],  # : <<<< controls
        )      #: <<<< column


class Build_Editor(ft.Container):
    """
    MAIN BUILDER EDITOR: IT'S A ROW CONTAINER THAT WILL CONTENT ALL WIDGET INSIDE WILL CALL BoxConfigContainer
    FUNCTION THAT HAVE THE BOX TO SHOW ASACTLY THE WIDGET ATTRIBUTES TO MODIFY

    Tabs:
       Container:
               edit_Container: value
       Widget:
               edit_Widget: value

    NOTE:
       Is necessary put class widget of the widget to edit Attributes
    """

    def __init__(self,
                 widget: object = None,
                 page: object = None,
                 main_phone: object = None,
                 ):

        super().__init__()
        #: VERY IMPORTANT
        #: WIDGET PHONE SELECTED TO MODIFY ATTRIBUTES
        self.widget = widget
        self.page = page
        self.main_phone = main_phone
        self.padding = ft.padding.all(0)
        self.margin = ft.margin.all(6)
        self.border_radius = ft.border_radius.all(28)
        self.alignment = ft.alignment.center
        self.width = 355
        self.height = 670
        self.show_tab = True
        # self.bgcolor = "grey"
        # self.bgcolor = "Black12"
        self.gradient = ft.LinearGradient(begin=ft.alignment.top_center, end=ft.alignment.bottom_center, colors=[
                                          ft.colors('black38'), ft.Colors.with_opacity(0.2, 'cyan'), ft.colors('black38')],)
        self.blur = (4, 8)

        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=18,
            color=ft.Colors.with_opacity(0.8, ft.colors('black26')),
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )

    def build(self):
        """
        ALL IN THIS APP IS A MODULE THAT'S WAY YOU MAY TAKE THE PART THAT YOU WANT REBUILD

        widgets_dict <= IS A DICT THAT CONTAIN ALL WIDGET THAT ARE WATING TO SHOW BECOUS BY DEFAULD ARE VISIBLE = OFF
        """
        self.main_phone = self.page.session.get(
            'SELECTED_SCREEN')                # main_phone

        self.phone_layer = self.main_phone.content.content.content
        self.main_phone_container = self.phone_layer               # main_phone_container
        # main_phone_container_content
        self.main_phone_container_content = self.phone_layer.content

        # SET DEFOULD NONE
        self.container_widget = None                # main_phone
        self.container_widget_content = None                # main_phone

        widgets_dict = {

            #: ESPECIAL WIDGETS ONLY FOR PHONE
            'phone_image_src'    :SelectionButtonEntry(    config_widget='image_src'    ,page=self.page ,screen_phone=self.main_phone                  ,id_name_widget_dict='main_phone'),

            'phone_padding'      :FourEntry(      config_widget='padding'               ,page=self.page ,screen_phone=self.main_phone_container        ,id_name_widget_dict="main_phone_container"),

            'phone_image_opacity':SingleNumeberEntry( config_widget='image_opacity'     ,page=self.page ,screen_phone=self.main_phone                  ,id_name_widget_dict='main_phone'),
           'column_phone_spacing':SingleNumeberEntry( config_widget='spacing'           ,page=self.page ,screen_phone=self.main_phone_container_content ,id_name_widget_dict="main_phone_container_content"),

            'phone_bgcolor'      :ColorEntry(     config_widget='bgcolor'               ,page=self.page ,screen_phone=self.main_phone_container        ,id_name_widget_dict="main_phone_container"),

            'column_phone_wrap'  :BoolEntry(      config_widget='wrap'                  ,page=self.page ,screen_phone=self.main_phone_container_content ,id_name_widget_dict="main_phone_container_content"),
            'column_phone_tight' :BoolEntry(      config_widget='tight'                 ,page=self.page ,screen_phone=self.main_phone_container_content ,id_name_widget_dict="main_phone_container_content"),
            'column_phone_scroll':BoolEntry(      config_widget='scroll'                ,page=self.page ,screen_phone=self.main_phone_container_content ,id_name_widget_dict="main_phone_container_content"),

            'phone_image_fit'    :SelectionEntry( config_widget='image_fit'             ,page=self.page ,screen_phone=self.main_phone                   ,id_name_widget_dict='main_phone'),
        'column_phone_alignment' :SelectionEntry( config_widget='alignment'             ,page=self.page ,screen_phone=self.main_phone_container_content ,id_name_widget_dict="main_phone_container_content"),
   'column_horizontal_alignment' :SelectionEntry( config_widget='horizontal_alignment'  ,page=self.page ,screen_phone=self.main_phone_container_content ,id_name_widget_dict="main_phone_container_content"),

            'phone_gradient'     :GradientEntry(  config_widget='gradient'              ,page=self.page ,screen_phone=self.main_phone                  ,id_name_widget_dict='main_phone'),
            'phone_blur'         :DoubleEntry(    config_widget='blur'                  ,page=self.page ,screen_phone=self.main_phone_container        ,id_name_widget_dict="main_phone_container"),

        #: ESPECIAL WIDGETS ONLY FOR CONTAINERS

        'container_rotate'   :SingleNumeberEntry(    config_widget='rotate'         ,page=self.page ,screen_phone=self.container_widget),
        'container_scale'    :SingleNumeberEntry(    config_widget='scale'          ,page=self.page ,screen_phone=self.container_widget),
        'container_padding'  :FourEntry(      config_widget='padding'               ,page=self.page ,screen_phone=self.container_widget),
        'container_margin'   :FourEntry(      config_widget='margin'                ,page=self.page ,screen_phone=self.container_widget),
        'container_offset'   :DoubleEntry(    config_widget='offset'                ,page=self.page ,screen_phone=self.container_widget),
        'container_alignment':SelectionEntry( config_widget='alignment '            ,page=self.page ,screen_phone=self.container_widget),

        'container_width'    :DoubleEntry(    config_widget='width'                 ,page=self.page ,screen_phone=self.container_widget),
        'container_border'   :DoubleEntry(    config_widget='border'                ,page=self.page ,screen_phone=self.container_widget),
        'container_expand'   :BoolEntry(      config_widget='expand'                ,page=self.page ,screen_phone=self.container_widget),
        'container_ink'      :BoolEntry(      config_widget='ink'                   ,page=self.page ,screen_phone=self.container_widget),
        'container_visible'  :BoolEntry(      config_widget='visible'               ,page=self.page ,screen_phone=self.container_widget),
        'container_border_radius':FourEntry(      config_widget='border_radius'         ,page=self.page ,screen_phone=self.container_widget),

        'container_blur'     :DoubleEntry(    config_widget='blur'                  ,page=self.page ,screen_phone=self.container_widget),
        'container_bgcolor'  :ColorEntry(     config_widget='bgcolor'               ,page=self.page ,screen_phone=self.container_widget),
        'BlurColorEntry'     :BlurColorEntry( config_widget='blur'                  ,page=self.page ,screen_phone=self.container_widget),

        'shadow_color'       :ColorEntry(     config_widget='shadow_color'          ,page=self.page ,screen_phone=self.container_widget),
        'container_gradient' :GradientEntry(  config_widget='gradient'              ,page=self.page ,screen_phone=self.container_widget),

    'container_image_src'    :SelectionButtonEntry(    config_widget='image_src'   ,page=self.page ,screen_phone=self.container_widget),
    'container_image_opacity':SingleNumeberEntry(    config_widget='image_opacity' ,page=self.page ,screen_phone=self.container_widget),
    'container_image_fit'    :SelectionEntry( config_widget='image_fit'            ,page=self.page ,screen_phone=self.container_widget),

           'mix_widget' :DualNumeberEntry( config_widget='mix_container'        ,page=self.page ,screen_phone=self.container_widget ,         id_name_widget_dict='width'),
     'mix_widg_content' :DualNumeberEntry( config_widget='mix_container_content',page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='offset'),

        #: ESPECIAL WIDGETS ONLY FOR WIDGET
        'text'                :SingleEntry(config_widget='text'               ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='text'),
        'name'                :SingleEntry(config_widget='name'               ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='name'),
        'label'               :SingleEntry(config_widget='label'              ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='label'),
        'value'               :SingleEntry(config_widget='value'              ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='value'),

        'hint_text'           :SingleEntry(config_widget='hint_text'          ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='hint_text'),
        'counter_text'        :SingleEntry(config_widget='counter_text'       ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='counter_text'),
        'suffix_text'         :SingleEntry(config_widget='suffix_text'        ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='suffix_text'),
        'url'                 :SingleEntry(config_widget='url'                ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='url'),
        'url_target'          :SingleEntry(config_widget='url_target'         ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='url_target'),
        'icon'                :SingleEntry(config_widget='icon'               ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='icon'),
        'tooltip'             :SingleEntry(config_widget='tooltip'            ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='tooltip'),
        'data'                :SingleEntry(config_widget='data'               ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='data'),
        'semantics_label'     :SingleEntry(config_widget='semantics_label'    ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='semantics_label'),
        'src_base64'          :SingleEntry(config_widget='src_base64'         ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='src_base64'),
        'blur_radius'         :SingleEntry(config_widget='blur_radius'        ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='blur_radius'),

        #: INT AND FLOAT NUMBERS
        'size'                :SingleNumeberEntry(config_widget='size'               ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='size'),
        'spread_radius'       :SingleNumeberEntry(config_widget='spread_radius'      ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='spread_radius'),
        'elevation'           :SingleNumeberEntry(config_widget='elevation'          ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='elevation'),
        'rotate'              :SingleNumeberEntry(config_widget='rotate'             ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='rotate'),
        'scale'               :SingleNumeberEntry(config_widget='scale'              ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='scale'),
        'aspect_ratio'        :SingleNumeberEntry(config_widget='aspect_ratio'       ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='aspect_ratio'),
        'runs_count'          :SingleNumeberEntry(config_widget='runs_count'         ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='runs_count'),
        'run_spacing'         :SingleNumeberEntry(config_widget='run_spacing'        ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='run_spacing'),
        'spacing'             :SingleNumeberEntry(config_widget='spacing'            ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='spacing'),
        'child_aspect_ratio'  :SingleNumeberEntry(config_widget ='child_aspect_ratio',page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='child_aspect_ratio'),
        'max_extent'          :SingleNumeberEntry(config_widget='max_extent'         ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='max_extent'),
        'min_lines'           :SingleNumeberEntry(config_widget='min_lines'          ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='min_lines'),
        'max_lines'           :SingleNumeberEntry(config_widget='max_lines'          ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='max_lines'),
        'border_width'        :SingleNumeberEntry(config_widget='border_width'       ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='border_width'),
        'text_size'           :SingleNumeberEntry(config_widget='text_size'          ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='text_size'),
        'image_opacity'       :SingleNumeberEntry(config_widget='image_opacity'      ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='image_opacity'),
        'opacity'             :SingleNumeberEntry(config_widget='opacity'            ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='opacity'),

        #: SELECTION BUTTOM ENTRY
        'src'                 :SelectionButtonEntry(config_widget='src'       ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='src'),
        'image_src'           :SelectionButtonEntry(config_widget='image_src' ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='image_src'),

        #: DOUBLE SELECTION ENTRY

        'width'               :DoubleEntry(config_widget='width'              ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='width'),
        'border'              :DoubleEntry(config_widget='border'             ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='border'),
        'offset'              :DoubleEntry(config_widget='offset'             ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='offset'),
        'blur'                :DoubleEntry(config_widget='blur'               ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='blur'),

        #: 4 SELECTION ENTRIE S

        'padding'             :FourEntry(config_widget='padding'              ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='padding'),
        'margin'              :FourEntry(config_widget='margin'               ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='margin'),
        'border_radius'       :FourEntry(config_widget='border_radius'        ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='border_radius'),

        #: COLOR ENTRY ['RED' ...]

        'bgcolor'             :ColorEntry(config_widget= 'bgcolor'            ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='bgcolor'),
        'color'               :ColorEntry(config_widget= 'color'              ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='color'),
        'icon_color'          :ColorEntry(config_widget= 'icon_color'         ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='icon_color'),
        'check_color'         :ColorEntry(config_widget= 'check_color'        ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='check_color'),
        'fill_color'          :ColorEntry(config_widget= 'fill_color'         ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='fill_color'),
        'border_color'        :ColorEntry(config_widget= 'border_color'       ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='border_color'),
        'focused_bgcolor'     :ColorEntry(config_widget= 'focused_bgcolor'    ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='focused_bgcolor'),
        'focused_border_color':ColorEntry(config_widget= 'focused_border_color',page=self.page ,screen_phone=self.container_widget_content, id_name_widget_dict='focused_border_color'),
        'box_shadow'          :ColorEntry(config_widget= 'box_shadow',         page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='box_shadow'),

        #: BOOL ENTRY [TRUE FALSE]

        'expand':             BoolEntry(config_widget='expand'                 ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='expand'),
        'ink':                BoolEntry(config_widget='ink'                    ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='ink'),
        'scroll':             BoolEntry(config_widget='scroll'                 ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='scroll'),
        'wrap':               BoolEntry(config_widget='wrap'                   ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='wrap'),
        'tight':              BoolEntry(config_widget='tight'                  ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='tight'),
        'visible':            BoolEntry(config_widget='visible'                ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='visible'),
        'multiline':          BoolEntry(config_widget='multiline'              ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='multiline'),
        'disabled':           BoolEntry(config_widget='disabled'               ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='disabled'),
        'read_only':          BoolEntry(config_widget='read_only'              ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='read_only'),
        'password':           BoolEntry(config_widget='password'               ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='password'),
        'filled':             BoolEntry(config_widget='filled'                 ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='filled'),
        'adaptive':           BoolEntry(config_widget='adaptive'               ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='adaptive'),
        'tristate':           BoolEntry(config_widget='tristate'               ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='tristate'),
        'autofocus':          BoolEntry(config_widget='autofocus'              ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='read_only'),
        'horizontal':         BoolEntry(config_widget='horizontal'             ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='horizontal'),
        'can_reveal_password':BoolEntry(config_widget='can_reveal_password'    ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='can_reveal_password'),
        'capitalization':     BoolEntry(config_widget='capitalization'         ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='capitalization'),
        'gapless_playback':   BoolEntry(config_widget='gapless_playback'       ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='gapless_playback'),

        #: SELECTION ENTRY

        'image_fit':          SelectionEntry(config_widget='image_fit'           ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='image_fit'),
        'image_fit_src':      SelectionEntry(config_widget='image_fit_src'       ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='src'),
        'weight':             SelectionEntry(config_widget='weight'              ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='weight'),
        'keyboard_type':      SelectionEntry(config_widget='keyboard_type'       ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='keyboard_type'),
        'text_align':         SelectionEntry(config_widget='text_align'          ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='text_align'),
        'alignment':          SelectionEntry(config_widget='alignment'           ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='alignment'),
        'content_alignment':  SelectionEntry(config_widget='content_alignment'   ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='content_alignment'),
        'vertical_alignment' :SelectionEntry(config_widget='vertical_alignment'  ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='vertical_alignment'),
        'horizontal_alignment':SelectionEntry(config_widget='horizontal_alignment',page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='horizontal_alignment'),

        #: GRADIEN ENTRY

        'gradient':           GradientEntry(config_widget ='gradient'            ,page=self.page ,screen_phone=self.container_widget_content , id_name_widget_dict='gradient'),
        }

        self.check_width_page = self.check_size_page()

        self.main_phone_tab_1 = ft.Container(
            # bgcolor="red",
            padding=ft.padding.only(
                left=4,
                top=4,
                right=4,
                bottom=4),
            # size=0.5,
            content=ft.Column(
                scroll="HIDDEN",
                controls=[
                    BoxConfigContainer(
                        size_screen=self.check_width_page,
                        title='Color Phone Container',
                        controls=[
                            widgets_dict.get('phone_blur'),
                            widgets_dict.get('phone_bgcolor'),
                            widgets_dict.get('phone_gradient'),
                            widgets_dict.get('phone_padding'),
                        ],),

                    BoxConfigContainer(
                        size_screen=self.check_width_page,
                        title='Image Phone Container',
                        controls=[
                            widgets_dict.get('phone_image_src'),
                            widgets_dict.get('phone_image_fit'),
                            widgets_dict.get('phone_image_opacity'),
                        ],),

                    # BoxConfigContainer(
                    #     size_screen=self.check_width_page,
                    #     title='Column Phone Property',
                    #     controls=[
                    #         widgets_dict.get('column_phone_tight'),
                    #         widgets_dict.get('column_phone_wrap'),
                    #         widgets_dict.get('column_phone_scroll'),
                    #         widgets_dict.get('column_phone_spacing'),
                    #         widgets_dict.get('column_phone_alignment'),
                    #         widgets_dict.get('column_horizontal_alignment'),
                    #     ],),
                ],
            ),
        )

        self.widget_container = ft.Container(
            padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
            visible=False,
            content=ft.Column(
                scroll="HIDDEN",
                controls=[
                    BoxConfigContainer(
                        size_screen=self.check_width_page,
                        title='Color Container',
                        controls=[
                            widgets_dict.get('BlurColorEntry'),
                            widgets_dict.get('mix_widget'),
                            widgets_dict.get('container_gradient'),
                            widgets_dict.get('container_ink'),
                            widgets_dict.get('container_bgcolor'),
                            widgets_dict.get('shadow_color'),


                        ],),

                    BoxConfigContainer(
                        size_screen=self.check_width_page,
                        title='Image Container',
                        controls=[
                            widgets_dict.get('container_image_src'),
                            widgets_dict.get('container_image_fit'),
                            widgets_dict.get('container_image_opacity'),

                        ],),

                    BoxConfigContainer(
                        size_screen=self.check_width_page,
                        title='Position Container',
                        controls=[
                            widgets_dict.get('container_padding'),
                            widgets_dict.get('container_margin'),
                            widgets_dict.get('container_border_radius'),
                            widgets_dict.get('container_border'),
                            widgets_dict.get('container_rotate'),
                            widgets_dict.get('container_scale'),
                            widgets_dict.get('container_offset'),
                            widgets_dict.get('container_alignment'),
                        ],),

                    BoxConfigContainer(
                        size_screen=self.check_width_page,
                        title='Modification Container',
                        controls=[
                            widgets_dict.get('container_width'),
                            widgets_dict.get('container_expand'),
                            widgets_dict.get('container_visible'),
                        ],),

                ],
            ),
        )

        self.widget_container_content = ft.Container(
            padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
            visible=False,

            content=ft.Column(
                scroll="HIDDEN",
                controls=[

                    BoxConfigContainer(
                        size_screen=self.check_width_page,
                        title='Input Text Data',
                        controls=[
                            widgets_dict.get('mix_widg_content'),

                            widgets_dict.get('src'),
                            widgets_dict.get('image_fit_src'),
                            widgets_dict.get('opacity'),
                            widgets_dict.get('image_src'),
                            widgets_dict.get('image_fit'),
                            widgets_dict.get('image_opacity'),
                            widgets_dict.get('src_base64'),

                            widgets_dict.get('text'),
                            widgets_dict.get('name'),
                            widgets_dict.get('label'),
                            widgets_dict.get('data'),
                            widgets_dict.get('value'),
                            widgets_dict.get('url'),
                            widgets_dict.get('url_target'),

                        ],),

                    BoxConfigContainer(
                        size_screen=self.check_width_page,
                        title='Colors Widget in Box',
                        controls=[
                            widgets_dict.get('color'),
                            widgets_dict.get('bgcolor'),
                            widgets_dict.get('icon_color'),
                            widgets_dict.get('check_color'),
                            widgets_dict.get('fill_color'),
                            widgets_dict.get('shadow_color'),
                            widgets_dict.get('focused_bgcolor'),
                            widgets_dict.get('border_color'),
                            widgets_dict.get('focused_border_color'),
                        ],),

                    BoxConfigContainer(
                        size_screen=self.check_width_page,
                        title='Position Widget in Box',
                        controls=[
                            widgets_dict.get('padding'),
                            widgets_dict.get('margin'),
                            widgets_dict.get('border_radius'),
                            widgets_dict.get('spacing'),
                            widgets_dict.get('offset'),
                            widgets_dict.get('rotate'),
                            widgets_dict.get('runs_count'),
                            widgets_dict.get('run_spacing'),
                            widgets_dict.get('elevation'),
                            widgets_dict.get('keyboard_type'),
                            widgets_dict.get('alignment'),
                            widgets_dict.get('vertical_alignment'),
                            widgets_dict.get('horizontal_alignment'),
                            widgets_dict.get('horizontal'),
                            widgets_dict.get('filled'),
                        ],),

                    BoxConfigContainer(
                        size_screen=self.check_width_page,
                        title='Modification Size Widget',
                        controls=[
                            widgets_dict.get('width'),
                            widgets_dict.get('size'),
                            widgets_dict.get('scale'),
                            widgets_dict.get('aspect_ratio'),
                            widgets_dict.get('child_aspect_ratio'),
                            widgets_dict.get('max_extent'),
                            widgets_dict.get('wrap'),
                            widgets_dict.get('adaptive'),
                            widgets_dict.get('expand'),
                            widgets_dict.get('tight'),
                        ],),

                    BoxConfigContainer(
                        size_screen=self.check_width_page,
                        title='Modification Widget',
                        controls=[
                            widgets_dict.get('visible'),
                            widgets_dict.get('disabled'),
                            widgets_dict.get('read_only'),
                            widgets_dict.get('autofocus'),
                            widgets_dict.get('ink'),
                            widgets_dict.get('scroll'),
                            widgets_dict.get('tristate'),
                            widgets_dict.get('gapless_playback'),
                        ],),

                    BoxConfigContainer(
                        size_screen=self.check_width_page,
                        title='Modification Text Data',
                        controls=[
                            widgets_dict.get('text_size'),
                            widgets_dict.get('hint_text'),
                            widgets_dict.get('min_lines'),
                            widgets_dict.get('max_lines'),
                            widgets_dict.get('counter_text'),
                            widgets_dict.get('semantics_label'),
                            widgets_dict.get('suffix_text'),
                            widgets_dict.get('text_align'),
                            widgets_dict.get('weight'),
                            widgets_dict.get('multiline'),
                            widgets_dict.get('capitalization'),
                            widgets_dict.get('password'),
                            widgets_dict.get('can_reveal_password'),
                        ],),

                    BoxConfigContainer(
                        size_screen=self.check_width_page,
                        title='Modification Border Widget Box',
                        controls=[
                            widgets_dict.get('border'),
                            widgets_dict.get('spread_radius'),
                            widgets_dict.get('border_width'),
                        ],),


                    BoxConfigContainer(
                        size_screen=self.check_width_page,
                        title='Icon or Image in Box',
                        controls=[
                            widgets_dict.get('icon'),
                            widgets_dict.get('blur'),
                            widgets_dict.get('blur_radius'),
                        ],),
                ],
            ),
        )
        self.photo_selection = ScreenPhotoSelection()
        self.color_selection = Screen_palette()

        self.content = ft.Stack(
            controls=[
                ft.Tabs(
                    label_color='BLUE',
                    indicator_border_radius=ft.border_radius.all(20),
                    tabs=[

                        ft.Tab(
                            text="Box Phone",

                            content=self.main_phone_tab_1
                        ),
                        ft.Tab(
                            text="Box Container",
                            content=self.widget_container
                        ),
                        ft.Tab(
                            text="Box Widget",
                            content=self.widget_container_content,
                        ),
                    ],
                ),
                self.photo_selection,
                self.color_selection,
            ],
        )
        self.photo_selection.visible = False
        self.color_selection.visible = False
        self.page.session.set('PHOTO_SELECTION', self.content)

        # SETTING GLOVAL VAR OF PHONE CONTAINER
        self.page.session.set('DICT_WIDGETS', self.widget)
        self.page.session.set("CONFIG_TABS_CONTAINERS", self.widget_container)
        self.page.session.set(
            "CONFIG_TABS_CONTAINERS_CONTENT", self.widget_container_content)

    def check_size_page(self):
        page_width = self.page.width
        if page_width == 0:
            return 350

        if page_width <= 690.0:
            # self.visible = False
            # return 270
            self.width = 260

        return 350

if __name__ == '__main__':
    def main(page: ft.Page):
        page.scroll = "HIDDEN"  # AUTO ADAPTIVE ALWAYS HIDDEN
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode = ft.ThemeMode.DARK  # ft.ThemeMode.LIGHT
        page.window_bgcolor = ft.colors.RED_100
        page.window_left = 3
        page.window_top = 3
        page.window_height = 680
        page.window_width = 370
        page.padding = 0
        page.spacing = 0
        page.add(Build_Editor(widget=ft.Container()))

    ft.app(target=main)
