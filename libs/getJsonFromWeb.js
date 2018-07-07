/**
 * Created by Administrator on 2018/7/4/004.
 */

(function ($) {
    var tables, dist = [], subDist = {watchType: '', info: []}, thirdDist = {title: '', body: []};
    tables = $(".whole-row");
    $.each(tables, function (i, n) {
        dataLevel = parseInt($(n).attr("data-level"));
        if (dataLevel !== 1) {
            if (dataLevel == 2 && subDist.watchType == '') {
                labelItem2 = $(n).find(".force-wrap .white-space").text();
                subDist.watchType = labelItem2;
            } else if (dataLevel == 2) {
                // console.log('======');
                dist.push(subDist);
                labelItem2 = $(n).find(".force-wrap .white-space").text();
                subDist = {watchType: '', info: []};
                subDist.watchType = labelItem2;
            } else {
                //console.log(dataLevel);
                if (dataLevel == 3) {
                    if (thirdDist.title == '') {
                        labelItem3 = $(n).find(".force-wrap .white-space").text();
                        thirdDist.title = labelItem3;
                    } else {
                        //已经添加完level4的数据
                        subDist.info.push(thirdDist);
                        thirdDist = {title: '', body: []}
                    }
                } else if (dataLevel == 4) {
                    labelItem4 = $(n).find(".force-wrap .white-space").text();
                    thirdDist.body.push(labelItem4);
                }
            }


        }
    });
    dist.push(subDist);
    console.log(JSON.stringify(dist));
})(window.jQuery);