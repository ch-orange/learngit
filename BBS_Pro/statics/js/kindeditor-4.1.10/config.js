KindEditor.ready(function(K) {
                 K.create('textarea[name=message]',{
                	width:800,
                	height:200,
                	uploadJson: '/admin/upload/kindeditor',
                });
        });