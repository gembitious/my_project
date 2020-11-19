$(function () {

    function checkName(obj, target) {
        let x = $(obj).val();
        let id = $('#' + target + " > option:contains(" + x + ")").val();
        $('#' + target).val(id).prop("selected", true);
    }

    function setPokemonListNonDup() {
        $('#selectPokemon').empty();
        let cup = $('#cup').val();
        $.ajax({
            url: "../data/gamemaster.json",
            dataType: "json",
            data: {},
            success: function (res) {
                let dex = res["pokemon"]
                let pokeList = ``;
                for (let i = 0; i < dex.length; i++) {
                    let id = dex[i]["speciesId"];
                    let nameKor = dex[i]["speciesNameKor"];
                    let nameEng = dex[i]["speciesName"];
                    let temp = `<option value="${id}">${nameKor} / ${nameEng}</option>`;
                    if (id.indexOf('_') == -1) {
                        pokeList += temp;
                    }
                }
                $('#selectPokemon').append(pokeList);
            }
        });
    }
})