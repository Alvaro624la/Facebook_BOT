class PopUpsClass():
    def CREDENTIALS(info_to_user_message):
        return f"""
            let html_user_credentials_cont_1 = document.createElement('div');
            html_user_credentials_cont_1.style.cssText = `
                color: #fff;
                position: fixed; 
                top: 0; 
                left: 0;
                width: 100%;
                height: 100%;
                display: flex;
                flex-direction: column;
                padding: 90px 0 0 2em; 
                background-color: #0c0c0c; 
                z-index: 9998;
                overflow-y: auto
            `; 
            document.body.appendChild(html_user_credentials_cont_1);

            let credenciales_introducidos = document.createElement('p');
            credenciales_introducidos.id = 'credenciales_introducidos';
            credenciales_introducidos.innerHTML = 'False';
            credenciales_introducidos.style.cssText = `
                display: none;
            `;
            html_user_credentials_cont_1.appendChild(credenciales_introducidos);

            let html_user_message_cont_0 = document.createElement('p');
            html_user_message_cont_0.textContent = '{info_to_user_message}';
            html_user_message_cont_0.style.cssText = `
                color: #fff;
                font-size: 1.2em;
                padding: 0 1em;
                z-index: 9998
            `; 
            html_user_credentials_cont_1.appendChild(html_user_message_cont_0);
            
            let html_user_name_cont_1_1 = document.createElement('div'); 
            html_user_name_cont_1_1.style.cssText = `
                // width: 100%;
                display: flex;
                flex-direction: row;
                flex-wrap: wrap;
                align-items: center;
                z-index: 9998
            `; 
            html_user_credentials_cont_1.appendChild(html_user_name_cont_1_1);

            let html_user_name_label_cont_1_1_1 = document.createElement('p'); 
            html_user_name_label_cont_1_1_1.textContent = 'Usuario / Email';
            html_user_name_label_cont_1_1_1.style.cssText = `
                color: #fff;
                font-size: 1.1em;
                padding: 1em;
                border-radius: 5px; 
                z-index: 9998
                border: 1px solid green;
                width: 100px
            `; 
            html_user_name_cont_1_1.appendChild(html_user_name_label_cont_1_1_1);

            let html_user_name_input_cont_1_1_2 = document.createElement('input');
            html_user_name_input_cont_1_1_2.id = 'credentials_name_input';
            html_user_name_input_cont_1_1_2.style.cssText = `
                color: #000;
                font-size: 1.1em;
                padding: 1em; 
                background-color: #fff; 
                border-radius: 5px; 
                z-index: 9998;
                height: 6px;
                border: 2px solid #fff;
                border-radius: 5px
            `; 
            html_user_name_cont_1_1.appendChild(html_user_name_input_cont_1_1_2);

            let html_user_password_cont_1_2 = document.createElement('div'); 
            html_user_password_cont_1_2.style.cssText = `
                // width: 100%;
                display: flex;
                flex-direction: row;
                flex-wrap: wrap;
                align-items: center;
                z-index: 9998
            `; 
            html_user_credentials_cont_1.appendChild(html_user_password_cont_1_2);

            let html_user_password_label_cont_1_2_1 = document.createElement('p'); 
            html_user_password_label_cont_1_2_1.textContent = 'Contraseña';
            html_user_password_label_cont_1_2_1.style.cssText = `
                color: #fff;
                font-size: 1.1em;
                padding: 1em;
                border-radius: 5px; 
                z-index: 9998;
                width: 100px
            `; 
            html_user_password_cont_1_2.appendChild(html_user_password_label_cont_1_2_1);

            let html_user_password_input_cont_1_2_2 = document.createElement('input');
            html_user_password_input_cont_1_2_2.id = 'credentials_password_input'; 
            html_user_password_input_cont_1_2_2.style.cssText = `
                color: #000;
                font-size: 1.1em;
                padding: 1em;
                background-color: #fff; 
                border-radius: 5px; 
                z-index: 9998;
                height: 6px;
                border: 2px solid #fff;
                border-radius: 5px
            `; 
            html_user_password_cont_1_2.appendChild(html_user_password_input_cont_1_2_2);

            let html_credentials_button_cont_1_3 = document.createElement('button');
            html_credentials_button_cont_1_3.textContent = 'Aceptar';
            html_credentials_button_cont_1_3.style.cssText = `
                padding: 1em;
                background-color: #fff;
                color: #000;
                border-radius: 5px;
                z-index: 9998;
                border: 1px solid #000;
                width: 100px;
                height: 60px;
                cursor: pointer
            `;
            html_user_credentials_cont_1.appendChild(html_credentials_button_cont_1_3);

            html_credentials_button_cont_1_3.addEventListener('mouseenter', () => {{
                html_credentials_button_cont_1_3.style.cssText = `
                    padding: 1em;
                    background-color: #aaa;
                    color: #000;
                    border-radius: 5px;
                    z-index: 9998;
                    border: 1px solid #000;
                    width: 100px;
                    height: 60px;
                    cursor: pointer
                `;
            }});

            html_credentials_button_cont_1_3.addEventListener('mouseleave', () => {{
                html_credentials_button_cont_1_3.style.cssText = `
                    padding: 1em;
                    background-color: #fff;
                    color: #000;
                    border-radius: 5px;
                    z-index: 9998;
                    border: 1px solid #000;
                    width: 100px;
                    height: 60px;
                    cursor: pointer
                `;
            }});

            html_credentials_button_cont_1_3.addEventListener('mousedown', () => {{
                html_credentials_button_cont_1_3.style.cssText = `
                    transform: scale(0.95);
                    padding: 1em;
                    background-color: #aaa;
                    color: #000;
                    border-radius: 5px;
                    z-index: 9998;
                    border: 1px solid #000;
                    width: 100px;
                    height: 60px;
                    cursor: pointer
                `;
            }});

            html_credentials_button_cont_1_3.addEventListener('mouseup', () => {{
                html_credentials_button_cont_1_3.style.cssText = `
                    transform: scale(1);
                    padding: 1em;
                    background-color: #aaa;
                    color: #000;
                    border-radius: 5px;
                    z-index: 9998;
                    border: 1px solid #000;
                    width: 100px;
                    height: 60px;
                    cursor: pointer
                `;
            }});

            html_credentials_button_cont_1_3.addEventListener('click', () => {{
                html_user_credentials_cont_1.style.cssText = `
                    display: none;
                `;
                credenciales_introducidos.innerHTML = 'True';
            }});
        """
    def QUICK_MESSAGE(info_to_user_message):
        return f"""
            let html_mensaje = document.createElement('div'); 
            html_mensaje.textContent = '{info_to_user_message}'; 
            html_mensaje.style.cssText = `
                font-size: 1.2em; 
                position: fixed; 
                top: 15px; 
                left: 15px; 
                padding: 40px; 
                background-color: yellow; 
                border-radius: 5px; 
                z-index: 9999
            `; 
            document.body.appendChild(html_mensaje);
        """
    def GROUP_SELECTION(info_to_user_message, arr_obj_grupos_obtenidos):
        return f"""
            let html_seleccion_grupos_cont_1 = document.createElement('div');
            let html_info_to_user_message_cont_1_1 = document.createElement('p');
            html_seleccion_grupos_cont_1.appendChild(html_info_to_user_message_cont_1_1);
            html_seleccion_grupos_cont_1.innerHTML = '{info_to_user_message}';
            html_info_to_user_message_cont_1_1.style.cssText = `
                font-size: 1.2em;
                padding: 20px;
                background-color: yellow;
                border-radius: 5px;
                z-index: 9998
            `;

            // Loop en el arr de objetos y muestra cada uno con sus valores
            let arr = {arr_obj_grupos_obtenidos};

            let arr2 = [];
            let indicesTrue = [];
            let html_linkDivButtonDown_cont_1_2 = document.createElement('button');
            html_linkDivButtonDown_cont_1_2.textContent = 'Aceptar';
            html_seleccion_grupos_cont_1.appendChild(html_linkDivButtonDown_cont_1_2);
            html_linkDivButtonDown_cont_1_2.style.cssText = `
                padding: 1em;
                background-color: #fff;
                color: #000;
                border-radius: 5px;
                z-index: 9998;
                border: 1px solid #000;
                width: 100px;
                height: 60px;
                cursor: pointer
            `;
            let ids_ocultos = document.createElement('p');
            html_seleccion_grupos_cont_1.appendChild(ids_ocultos);
            ids_ocultos.id = 'ids_ocultos';
            ids_ocultos.style.cssText = `
                display: none;
            `;

            let ids_ocultos_seleccionados = document.createElement('p');
            html_seleccion_grupos_cont_1.appendChild(ids_ocultos_seleccionados);
            ids_ocultos_seleccionados.id = 'ids_ocultos_seleccionados';
            ids_ocultos_seleccionados.style.cssText = `
                display: none;
            `;
            ids_ocultos_seleccionados.innerHTML = 'False';

            let html_linkDiv_cont_1_3 = document.createElement('div');
            html_linkDiv_cont_1_3.style.cssText = `
                width: 100%;
                display: flex;
                flex-direction: row;
                flex-wrap: wrap;
                padding: 2em; 
                background-color: #0c0c0c; 
                z-index: 9998;
                overflow-y: scroll
            `;
            html_seleccion_grupos_cont_1.appendChild(html_linkDiv_cont_1_3);

            for (let i = 0; i < arr.length; i++) {{
                let html_linkDiv_1_3_1 = document.createElement('div');        
                // html_linkDiv_1_3_1.innerHTML = '<p>' + arr[i].index + '</p>' + '<img src="' + arr[i].img_url + '"/>' + '<p>' + arr[i].title + '</p>';
                html_linkDiv_1_3_1.innerHTML = '<img src="' + arr[i].img_url + '"/>' + '<p>' + arr[i].title + '</p>';
                html_linkDiv_cont_1_3.appendChild(html_linkDiv_1_3_1);

                html_linkDiv_1_3_1.style.cssText = `
                    color: #000;
                    width: 100px;
                    height: 200px;
                    padding: 1em;
                    background-color: #0d0;
                    border-radius: 5px;
                    z-index: 9998;
                    border: 1px solid #000;
                    cursor: pointer
                `;
                
                html_linkDiv_1_3_1.addEventListener('click', () => {{
                    arr2[arr[i].index].seleccionado ? (
                            arr2[arr[i].index].seleccionado = false,
                            html_linkDiv_1_3_1.style.backgroundColor = '#d00'
                        ) : (
                            arr2[arr[i].index].seleccionado = true,
                            html_linkDiv_1_3_1.style.backgroundColor = '#0d0'
                        );
                }});
                arr2.push({{
                    grupo_index: i,
                    seleccionado: true
                }});
            }}
            html_linkDivButtonDown_cont_1_2.addEventListener('mouseenter', () => {{
                html_linkDivButtonDown_cont_1_2.style.cssText = `
                    padding: 1em;
                    font-size: 1.2em;
                    background-color: #aaa;
                    color: #000;
                    border-radius: 5px;
                    z-index: 9998;
                    border: 1px solid #000;
                    width: 100px;
                    height: 60px;
                    cursor: pointer
                `;
            }});

            html_linkDivButtonDown_cont_1_2.addEventListener('mouseleave', () => {{
                html_linkDivButtonDown_cont_1_2.style.cssText = `
                    padding: 1em;
                    font-size: 1.2em;
                    background-color: #fff;
                    color: #000;
                    border-radius: 5px;
                    z-index: 9998;
                    border: 1px solid #000;
                    width: 100px;
                    height: 60px;
                    cursor: pointer
                `;
            }});

            html_linkDivButtonDown_cont_1_2.addEventListener('mousedown', () => {{
                html_linkDivButtonDown_cont_1_2.style.cssText = `
                    transform: scale(0.95);
                    padding: 1em;
                    font-size: 1.2em;
                    background-color: #fff;
                    color: #000;
                    border-radius: 5px;
                    z-index: 9998;
                    border: 1px solid #000;
                    width: 100px;
                    height: 60px;
                    cursor: pointer
                `;
            }});

            html_linkDivButtonDown_cont_1_2.addEventListener('mouseup', () => {{
                html_linkDivButtonDown_cont_1_2.style.cssText = `
                    transform: scale(1);
                    padding: 1em;
                    font-size: 1.2em;
                    background-color: #fff;
                    color: #000;
                    border-radius: 5px;
                    z-index: 9998;
                    border: 1px solid #000;
                    width: 100px;
                    height: 60px;
                    cursor: pointer
                `;
            }});
            html_linkDivButtonDown_cont_1_2.addEventListener('click', () => {{
                ids_ocultos.innerHTML = '';
                arr2.forEach(obj => {{
                    if(obj.seleccionado === true){{
                        ids_ocultos.innerHTML += obj.grupo_index + ', ';
                    }};
                }});
                html_seleccion_grupos_cont_1.style.cssText = `
                    display: none;
                `;
                ids_ocultos_seleccionados.innerHTML = 'True';
            }});
            html_seleccion_grupos_cont_1.style.cssText = `
                color: #fff;
                font-size: 1.2em;
                position: fixed; 
                top: 0; 
                left: 0;
                width: 100%;
                height: 100%;
                display: flex;
                flex-direction: column;
                padding: 2em; 
                background-color: #0c0c0c; 
                z-index: 9998;
            `;
            document.body.appendChild(html_seleccion_grupos_cont_1);
        """
    def CREATE_POST(info_to_user_message):
        return f"""
            let html_create_post_cont_1 = document.createElement('div');
            html_create_post_cont_1.style.cssText = `
                color: #fff;
                position: fixed; 
                top: 0; 
                left: 0;
                width: 100%;
                height: 100%;
                display: flex;
                flex-direction: column;
                padding: 90px 0 0 2em; 
                background-color: #0c0c0c;
                z-index: 9998;
                overflow-y: auto
            `;
            document.body.appendChild(html_create_post_cont_1);

            let post_creado = document.createElement('p');
            post_creado.id = 'post_creado';
            post_creado.innerHTML = 'False';
            post_creado.style.cssText = `
                display: none;
            `;
            html_create_post_cont_1.appendChild(post_creado);

            let html_create_post_mensaje_cont_1_1 = document.createElement('p');
            html_create_post_mensaje_cont_1_1.textContent = '{info_to_user_message}';
            html_create_post_mensaje_cont_1_1.style.cssText = `
                color: #fff;
                font-size: 1.2em;
                padding: 0 1em;
                z-index: 9998;
                overflow-y: scroll;
            `; 
            html_create_post_cont_1.appendChild(html_create_post_mensaje_cont_1_1);

            let html_create_post_input_cont_1_2 = document.createElement('textarea');
            html_create_post_input_cont_1_2.id = 'create_post_input';
            html_create_post_input_cont_1_2.style.cssText = `
                color: #000;
                font-size: 1.2em;
                padding: 2em;
                background-color: #fff; 
                border-radius: 5px; 
                z-index: 9998;
                border: 2px solid #fff;
                border-radius: 5px;
                width: 90%;
                min-height: 300px;
                max-height: 500px;
                spellcheck: true;
                resize: vertical
            `; 
            html_create_post_cont_1.appendChild(html_create_post_input_cont_1_2);

            let html_create_post_button_cont_1_3 = document.createElement('button');
            html_create_post_button_cont_1_3.textContent = 'Publicar';
            html_create_post_button_cont_1_3.style.cssText = `
                background-color: #22478e;
                padding: 1em;
                margin-top: 1em;
                color: #fff;
                border-radius: 5px;
                z-index: 9998;
                border: 3px solid #0b177b;
                font-size: 1.2em;
                width: 100px;
                height: 60px;
                cursor: pointer
            `;
            html_create_post_cont_1.appendChild(html_create_post_button_cont_1_3);

            html_create_post_button_cont_1_3.addEventListener('mouseenter', () => {{
                html_create_post_button_cont_1_3.style.cssText = `
                    background-color: #0b177b;
                    padding: 1em;
                    margin-top: 1em;
                    color: #fff;
                    border-radius: 5px;
                    z-index: 9998;
                    border: 3px solid #0b177b;
                    font-size: 1.2em;
                    width: 100px;
                    height: 60px;
                    cursor: pointer
                `;
            }});

            html_create_post_button_cont_1_3.addEventListener('mouseleave', () => {{
                html_create_post_button_cont_1_3.style.cssText = `
                    background-color: #22478e;
                    padding: 1em;
                    margin-top: 1em;
                    color: #fff;
                    border-radius: 5px;
                    z-index: 9998;
                    border: 3px solid #0b177b;
                    font-size: 1.2em;
                    width: 100px;
                    height: 60px;
                    cursor: pointer
                `;
            }});

            html_create_post_button_cont_1_3.addEventListener('mousedown', () => {{
                html_create_post_button_cont_1_3.style.cssText = `
                    transform: scale(0.95);
                    background-color: #0b177b;
                    padding: 1em;
                    margin-top: 1em;
                    color: #fff;
                    border-radius: 5px;
                    z-index: 9998;
                    border: 3px solid #0b177b;
                    font-size: 1.2em;
                    width: 100px;
                    height: 60px;
                    cursor: pointer
                `;
            }});

            html_create_post_button_cont_1_3.addEventListener('mouseup', () => {{
                html_create_post_button_cont_1_3.style.cssText = `
                    transform: scale(1);
                    background-color: #0b177b;
                    padding: 1em;
                    margin-top: 1em;
                    color: #fff;
                    border-radius: 5px;
                    z-index: 9998;
                    border: 3px solid #0b177b;
                    font-size: 1.2em;
                    width: 100px;
                    height: 60px;
                    cursor: pointer
                `;
            }});

            html_create_post_button_cont_1_3.addEventListener('click', () => {{
                html_create_post_cont_1.style.cssText = `
                    display: none;
                `;
                post_creado.innerHTML = 'True';
            }});
        """