| Actor | Descripción |
| ----- | ----------- |
| Usuario | Es el actor principal que usa la aplicación para comunicarse con otros usuarios, compartir mensajes, conectar con amigos, comentar publicaciones, seguir a otros usuarios, bloquear usuarios y eliminar sus propias publicaciones. |
| Administrador | Es el actor secundario que gestiona la aplicación, supervisa el contenido, modera los comentarios, elimina publicaciones inapropiadas y bloquea o desbloquea usuarios. |

| Caso de uso | Actor principal | Actor secundario | Descripción |
| ----------- | --------------- | ---------------- | ----------- |
| Publicar Mensaje | Usuario | - | El usuario crea y publica un mensaje en su perfil o en el de otro usuario. |
| Conectar con Amigos | Usuario | - | El usuario busca y envía solicitudes de amistad a otros usuarios, acepta o rechaza las solicitudes recibidas y ve su lista de amigos. |
| Eliminar Publicación | Usuario, Administrador | - | El usuario o el administrador elimina una publicación del perfil de un usuario. |
| Comentar Publicación | Usuario | Administrador | El usuario escribe y publica un comentario en una publicación de otro usuario. El administrador puede moderar los comentarios y eliminarlos si son ofensivos o inapropiados. |
| Seguir a otro Usuario | Usuario | - | El usuario sigue a otro usuario para ver sus publicaciones en su feed. |
| Bloquear Usuario | Usuario, Administrador | - | El usuario o el administrador bloquea a otro usuario para impedir que se comunique con él o vea su perfil. |
