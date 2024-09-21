"""
省去下载的麻烦，直接使用。
"""
import logging

logger = logging.getLogger(__name__)

english_stopwords = {'can', "hadn't", "you're", 'itself', "should've", 'only', 'shan', 'an', 's', 'and', 'me', 'ours',
                     'during', 'isn', 'has', 'does', 'while', "shouldn't", 'been', 'their', 'other', 'few', 'further',
                     'll', "didn't", 'he', 'hadn', 'as', 'some', 'to', 'between', 'too', 'same', 'where', "mustn't",
                     'off', 'again', 'are', 'ourselves', 'they', 'by', 'myself', 'yourself', 'am', 'is', 'above',
                     'weren', 'all', 'doesn', 'down', 'if', 'don', 'you', 'each', "won't", 'had', 'nor', 'ain', 'over',
                     'but', 'won', 'themselves', 'under', 'there', 'we', 'which', 'before', 'so', 've', "you'd", 'were',
                     'i', 'theirs', 'when', 'why', 'very', 'y', 'will', 'through', 'having', 'she', 'aren', "you've",
                     'out', 'who', 'with', 'd', 'mustn', 'not', "needn't", 'be', 'most', 'yourselves', 'herself',
                     'more', 't', 're', "mightn't", 'on', 'shouldn', "that'll", 'did', 'for', 'a', 'mightn', "aren't",
                     'needn', 'yours', 'how', 'because', 'him', 'here', "isn't", 'that', 'below', 'whom', 'couldn',
                     'up', "she's", 'hasn', 'of', "wouldn't", 'these', 'about', 'after', 'ma', 'm', 'o', "you'll",
                     'from', 'than', 'then', 'do', "wasn't", 'both', 'its', 'didn', 'no', 'such', "hasn't", "it's",
                     "couldn't", 'being', 'doing', 'into', 'should', 'those', "don't", "doesn't", 'it', 'haven', 'what',
                     'your', 'any', 'in', 'against', 'himself', 'this', 'them', 'his', 'hers', 'our', 'my', 'was',
                     "haven't", 'wouldn', "shan't", 'once', 'until', 'or', "weren't", 'the', 'have', 'at', 'her', 'own',
                     'just', 'now', 'wasn'}

chinese_stopwords = {'其余', '适应', '况且', '需要', '不过', '左右', '起见', '本着', '一直', '形成', '因此', '满足',
                     '以前', '立即', '重新', '倘或', '若是', '除', '喏', '他', '得出', '原来', '之类', '哗', '宁肯',
                     '万一', '他人', '其它', '实现', '或是', '这就是说', '随着', '相信', '强调', '嗡嗡', '开始', '并不',
                     '规定', '尽管', '哈哈', '哪些', '漫说', '第', '达到', '一定', '密切', '或者', '少数', '帮助',
                     '知道', '能否', '之前', '乃至', '本', '宣布', '真是', '故', '于是', '这儿', '以便', '并没有',
                     '考虑', '岂但', '由此可见', '但', '总结', '安全', '如下', '然而', '纵使', '必须', '反过来说',
                     '有所', '以後', '愿意', '这会儿', '顺', '各', '使得', '再者', '及其', '今天', '上去', '中间',
                     '合理', '最高', '要', '不问', '怎么', '跟', '这种', '加以', '不仅', '对于', '诸位', '练习', '逐渐',
                     '随', '要是', '后来', '那些', '在下', '大约', '以下', '咋', '一', '多数', '当着', '以至于', '表示',
                     '准备', '严格', '设若', '别说', '如其', '战斗', '而外', '特殊', '多少', '过', '行动', '咳', '就是',
                     '呜', '不能', '我', '有的', '这么些', '嘎登', '比较', '向', '扩大', '啊', '如此', '下来', '不变',
                     '与', '哟', '我的', '并', '喔唷', '不可', '觉得', '不单', '不一', '设使', '今后', '所有', '着呢',
                     '这么', '吗', '充分', '或', '无宁', '首先', '朝', '重大', '旁人', '其他', '应用', '这样', '之',
                     '也是', '哪个', '但是', '不够', '哦', '常常', '矣', '如', '许多', '积极', '叮咚', '开展', '呜呼',
                     '则', '不是', '高兴', '多', '不敢', '突出', '什么样', '此', '你的', '进步', '举行', '一方面',
                     '而言', '比', '而是', '先后', '过去', '极了', '何', '意思', '既是', '倘若', '其二', '与此同时',
                     '因而', '显然', '不同', '一样', '然则', '决定', '人们', '反应', '各级', '总的说来', '根本', '适用',
                     '上下', '何况', '如何', '欢迎', '倘使', '转贴', '啦', '那么些', '看来', '某些', '不久', '我们',
                     '的话', '趁', '这么点儿', '后面', '沿', '突然', '避免', '让', '慢说', '朝着', '何时', '纵然',
                     '每年', '自各儿', '可', '赶', '逐步', '认识', '可能', '叫做', '彼', '不会', '适当', '问题', '允许',
                     '己', '么', '虽然', '不足', '一边', '前后', '召开', '最好', '为了', '不如', '依照', '清楚', '于',
                     '怎样', '已经', '假如', '相当', '最近', '复杂', '总之', '并不是', '乌乎', '至', '反之', '不拘',
                     '专门', '为着', '必要', '不惟', '罢了', '而已', '嘘', '咚', '每个', '虽说', '目前', '一旦', '上述',
                     '咦', '特别是', '将', '自己', '不但', '各个', '好的', '没有', '更加', '不论', '维持', '与否', '啐',
                     '起', '你', '且', '通过', '是不是', '俺', '倘然', '彻底', '好象', '失去', '的', '等', '任', '吓',
                     '总是', '连同', '各位', '谁知', '要么', '下面', '处理', '同时', '自身', '之所以', '宁愿', '只是',
                     '变成', '不得', '防止', '比如', '当前', '哼', '今年', '等等', '以至', '假使', '遭到', '非徒',
                     '巨大', '同一', '打', '再说', '果真', '说明', '不然', '毋宁', '哎呀', '今後', '对应', '互相',
                     '也罢', '经常', '一片', '既', '进而', '接著', '某', '尽', '获得', '不只', '容易', '成为', '哪年',
                     '嗳', '以致', '能', '相反', '除非', '显著', '也', '相对而言', '自从', '相等', '主张', '构成',
                     '即或', '凭', '必然', '出去', '趁着', '哈', '进入', '到', '所谓', '通常', '嘻', '而况', '哎哟',
                     '这些', '整个', '其一', '看见', '争取', '纵', '各人', '往往', '造成', '真正', '为主', '强烈',
                     '当然', '哪样', '呢', '曾经', '加入', '固然', '方面', '它', '你们', '吧', '实际', '随著', '认为',
                     '有著', '深入', '代替', '一次', '几时', '所以', '一则', '加强', '吱', '要不是', '阿', '仍然',
                     '故此', '普通', '似的', '它的', '各自', '那麽', '一起', '甚至', '得到', '腾', '要不', '哪儿',
                     '之一', '这', '一些', '呗', '乘', '哎', '还是', '那样', '鄙人', '又', '行为', '具有', '一天',
                     '中小', '坚持', '那会儿', '每当', '为什么', '不成', '一般', '叫', '能够', '受到', '之后', '促进',
                     '即便', '限制', '什么', '可以', '不要', '相似', '冲', '它们的', '移动', '呃', '如若', '特点',
                     '从而', '啥', '咱', '最後', '有利', '如果', '只有', '几', '一面', '一下', '共同', '替', '别的',
                     '呼哧', '看看', '某个', '另外', '不比', '有力', '您', '来着', '以及', '现在', '呕', '上升', '哼唷',
                     '靠', '几乎', '别', '哇', '根据', '分别', '应该', '有', '怎么样', '给', '以后', '组成', '大批',
                     '若非', '即使', '喂', '过来', '沿着', '关于', '们', '全面', '丰富', '出来', '表明', '前者', '加之',
                     '俺们', '及时', '这时', '大力', '纵令', '结果', '从', '下去', '有着', '啪达', '直到', '即', '像',
                     '完全', '较之', '先後', '相同', '可是', '哪边', '他们', '该', '紧接着', '另', '一时', '出现',
                     '大大', '总而言之', '有关', '乎', '相应', '那', '集中', '任凭', '自个儿', '因为', '临', '却不',
                     '这个', '尚且', '地', '掌握', '正常', '使用', '望', '范围', '乃', '大家', '否则', '兮', '取得',
                     '看出', '做到', '自', '越是', '连', '至于', '那么样', '除此之外', '总的来看', '了', '虽', '附近',
                     '还有', '心里', '个人', '咱们', '除了', '也好', '部分', '哪', '她的', '向着', '开外', '这里',
                     '各种', '作为', '以为', '这点', '什麽', '在', '彼此', '认真', '于是乎', '此间', '由', '凭借',
                     '严重', '宁', '无论', '而', '其次', '引起', '直接', '每天', '较', '迅速', '遇到', '相对', '上来',
                     '嗯', '最大', '主要', '呸', '往', '继而', '正如', '呀', '运用', '之後', '一切', '方便', '自家',
                     '应当', '那个', '非常', '恰恰相反', '据', '是的', '经', '有点', '不断', '具体说来', '从事', '具体',
                     '谁', '不独', '哉', '个别', '看到', '完成', '两者', '反过来', '坚决', '与其', '而且', '嘿', '下列',
                     '其', '尤其', '边', '大量', '果然', '为何', '依', '当时', '既然', '甚而', '良好', '它们', '就',
                     '似乎', '属于', '前面', '她', '此外', '离', '以来', '另一方面', '为什麽', '即令', '即若', '她们',
                     '换句话说', '明显', '确定', '起来', '其中', '先生', '嗬', '当', '基本', '如上所述', '每', '宁可',
                     '不怕', '依靠', '接着', '正在', '前进', '采取', '怎', '来', '哩', '任何', '双方', '及至', '把',
                     '转变', '以免', '怎麽', '一来', '若', '被', '大多数', '重要', '吧哒', '这么样', '产生', '顺着',
                     '个', '後来', '上面', '就是说', '是', '经过', '甚么', '哪天', '焉', '进行', '哪怕', '同样', '抑或',
                     '那边', '这边', '归', '何处', '这麽', '那时', '十分', '比方', '管', '不光', '对', '那里', '所',
                     '用', '以上', '莫若', '论', '者', '鉴于', '绝对', '继续', '换言之', '冒', '按', '有些', '照',
                     '要不然', '综上所述', '为', '非但', '那么', '此时', '任务', '及', '存在', '拿', '明确', '结合',
                     '以', '以外', '例如', '广大', '现代', '全部', '有时', '嘎', '企图', '广泛', '怎么办', '和', '其实',
                     '各地', '转动', '联系', '注意', '要求', '然后', '具体地说', '有效', '按照', '省得', '那儿', '哪里',
                     '普遍', '时候', '同', '唉', '里面', '不管', '假若', '人家', '云云', '巩固', '保持', '并且', '待',
                     '然後', '了解', '後面', '可见', '无法', '一致', '伟大', '毫不', '照着', '倘', '周围', '呵', '嘛',
                     '因', '总的来说', '得', '最后', '反映', '只要', '只限', '着', '虽则', '由于', '多次', '是否',
                     '尔后', '不特', '他的'}

arabic_stopwords = {'تبدّل', 'اللتان', 'اثني', 'واو', 'حَذارِ', 'جنيه', 'ستة', 'أما', 'تشرين', 'كن', 'بئس', 'ورد',
                    'غدا', 'شين', 'هَاتِي', 'كم', 'إذن', 'بيد', 'ذواتي', 'ممن', 'أمد', 'مكانكما', 'لستم', 'إياي',
                    'ثالث', 'إياهما', 'عشر', 'سبحان', 'عل', 'هاكَ', 'خاصة', 'هما', 'شَتَّانَ', 'كيف', 'فبراير', 'مه',
                    'نون', 'ترك', 'ولكن', 'كرب', 'مازال', 'لاسيما', 'أفٍّ', 'مثل', 'لسنا', 'إليك', 'كليكما', 'زعم',
                    'مائة', 'أجمع', 'إي', 'كأين', 'نعم', 'قاف', 'بنا', 'أضحى', 'أسكن', 'بك', 'هيت', 'شرع', 'أمامك',
                    'أل', 'هناك', 'دينار', 'هلّا', 'بضع', 'أقل', 'دواليك', 'ثمّة', 'ثماني', 'أصبح', 'كلاهما', 'سقى',
                    'سبع', 'صباح', 'آه', 'كلَّا', 'سبعمائة', 'وَيْ', 'كأي', 'عدا', 'بي', 'بات', 'فيم', 'حاء', 'نبَّا',
                    'اتخذ', 'أخبر', 'ألفى', 'يمين', 'تفعلين', 'سبعمئة', 'إزاء', 'ذلكن', 'غير', 'عن', 'سوى', 'ابتدأ',
                    'لنا', 'أنتما', 'تموز', 'بما', 'هذا', 'هل', 'اثنان', 'أجل', 'بل', 'لي', 'ولا', 'جير', 'عامة', 'تلك',
                    'فلان', 'ما', 'لا', 'بعدا', 'وإذا', 'نوفمبر', 'ذ', 'إذما', 'أعطى', 'يوليو', 'يونيو', 'إليكما',
                    'كيت', 'كلّما', 'تَيْنِ', 'لو', 'بَسْ', 'فاء', 'اربعين', 'هذان', 'سبعين', 'جعل', 'هبّ', 'ب',
                    'يفعلان', 'نيف', 'ستون', 'يا', 'ي', 'ز', 'كلما', 'أخٌ', 'أولئك', 'حقا', 'كان', 'كِخ', 'أولالك',
                    'هيّا', 'لك', 'بخٍ', 'تخذ', 'آ', 'مليم', 'أربعمئة', 'عشرين', 'بَلْهَ', 'ليست', 'متى', 'إليكَ',
                    'ثمنمئة', 'تسعين', 'هيا', 'ثان', 'رزق', 'ر', 'جيم', 'سبعة', 'راح', 'بطآن', 'ث', 'تحوّل', 'أبدا',
                    'فو', 'أوشك', 'ارتدّ', 'حمو', 'هاهنا', 'جوان', 'علًّ', 'أين', 'آب', 'إيهٍ', 'هَيْهات', 'حاشا',
                    'سرعان', 'هَجْ', 'لهن', 'ما برح', 'من', 'كذا', 'بس', 'ألف', 'ليسوا', 'ء', 'طفق', 'ضحوة', 'لكنما',
                    'إذا', 'ثلاثمئة', 'أنبأ', 'تانِك', 'إيانا', 'عاد', 'وُشْكَانَ', 'قرش', 'ريث', 'شتانَ', 'أينما', 'ف',
                    'ثمانية', 'ط', 'تفعلون', 'أفعل به', 'خلف', 'أيها', 'باء', 'ذهب', 'اربعون', 'إمّا', 'عشرة', 'كأنّ',
                    'أنّى', 'تاسع', 'أي', 'أبو', 'ها', 'كل', 'ريال', 'دولار', 'لعمر', 'و', 'قبل', 'تِه', 'ثلاثون',
                    'اخلولق', 'أيّ', 'دال', 'شيكل', 'أربعاء', 'بهن', 'أنتن', 'مهما', 'ليت', 'حادي', 'أربع', 'نيسان',
                    'كأن', 'آهِ', 'همزة', 'لها', 'لا سيما', 'جانفي', 'شباط', 'خاء', 'خ', 'هَذانِ', 'كلا', 'ستمائة',
                    'قام', 'تلقاء', 'أى', 'له', 'اللتيا', 'تارة', 'هاتان', 'وما', 'ذين', 'عشرون', 'إياكن', 'إيه',
                    'تينك', 'إنا', 'تانِ', 'ظنَّ', 'إياكما', 'د', 'بلى', 'ثمانون', 'ءَ', 'إنما', 'إليكم', 'مادام',
                    'لولا', 'هي', 'هَاتِه', 'ثاني', 'انبرى', 'اللذان', 'ميم', 'فضلا', 'خمسون', 'زاي', 'خال', 'ذو',
                    'هلا', 'وإن', 'صبر', 'جويلية', 'ستين', 'صراحة', 'والذي', 'اللتين', 'ظلّ', 'بهما', 'حين', 'أربعمائة',
                    'ثلاثين', 'إلَيْكَ', 'هللة', 'ذه', 'فيها', 'ص', 'خلافا', 'لكي', 'صدقا', 'أمسى', 'ليس', 'ذال', 'ماي',
                    'ثاء', 'أن', 'مئة', 'بماذا', 'أمامكَ', 'درهم', 'صهْ', 'ذي', 'وإذ', 'ى', 'إياهن', 'لات', 'سحقا',
                    'عسى', 'هَذِه', 'وجد', 'مساء', 'عين', 'آذار', 'لستما', 'مرّة', 'عدَّ', 'أرى', 'ثم', 'هاتي', 'نَخْ',
                    'لعلَّ', 'آي', 'آنفا', 'أخذ', 'بعد', 'نحن', 'صاد', 'حسب', 'فمن', 'هاك', 'هاء', 'أنًّ', 'لستن',
                    'إياكم', 'عند', 'لسن', 'لما', 'هذي', 'حيث', 'إياك', 'حاي', 'حدَث', 'ل', 'ا', 'حرى', 'مئتان', 'حمٌ',
                    'ثلاثة', 'كما', 'فوق', 'حيثما', 'تسعمائة', 'إلى', 'ذِه', 'إذاً', 'ثمانين', 'هنالك', 'اللاتي', 'بها',
                    'لن', 'بين', 'درى', 'إلّا', 'حمدا', 'ما انفك', 'ولو', 'مكانَك', 'استحال', 'لدن', 'اثنا', 'عاشر',
                    'سبتمبر', 'لدى', 'طاء', 'ما أفعله', 'أوت', 'ّأيّان', 'لكما', 'الألاء', 'الآن', 'أصلا', 'بعض', 'ئ',
                    'إياه', 'ديسمبر', 'أنتم', 'أربعة', 'م', 'شتان', 'إنه', 'ض', 'ست', 'إليكنّ', 'كانون', 'رويدك', 'ذا',
                    'أكتوبر', 'فيفري', 'تسعون', 'ؤ', 'بسّ', 'رابع', 'ومن', 'لبيك', 'إن', 'راء', 'هذين', 'هَؤلاء',
                    'حبيب', 'هَذَيْنِ', 'ذانِ', 'خميس', 'ين', 'هَذا', 'حجا', 'جمعة', 'مكانكنّ', 'آض', 'عليك', 'في',
                    'خمسين', 'حزيران', 'أنتِ', 'ضاد', 'وهو', 'زود', 'صار', 'ذِي', 'خمسة', 'أم', 'لست', 'إما', 'لئن',
                    'حبذا', 'تاء', 'ذيت', 'تسع', 'أيضا', 'عليه', 'غداة', 'ليرة', 'ظاء', 'وراءَك', 'رأى', 'يورو', 'أنت',
                    'تحت', 'وهب', 'كسا', 'خامس', 'ذانك', 'علق', 'أيار', 'آناء', 'قطّ', 'إياهم', 'لكيلا', 'مذ', 'ذلكم',
                    'الذي', 'ستمئة', 'حار', 'ثامن', 'ظ', 'اللواتي', 'قاطبة', 'تين', 'ذات', 'هَاتَيْنِ', 'ماذا', 'حتى',
                    'لهما', 'بغتة', 'يوان', 'تفعلان', 'ن', 'رجع', 'كأيّن', 'تجاه', 'تعلَّم', 'بهم', 'ثمة', 'ج', 'طالما',
                    'على', 'هو', 'سين', 'لمّا', 'لكن', 'ثمَّ', 'لوما', 'مافتئ', 'ته', 'أغسطس', 'خلا', 'هاته', 'لكم',
                    'هاتين', 'ق', 'كاد', 'واهاً', 'ش', 'عيانا', 'صهٍ', 'هَذِي', 'يفعلون', 'طرا', 'أف', 'كي', 'الألى',
                    'بؤسا', 'كأنما', 'أيا', 'هؤلاء', 'كى', 'جلل', 'ذواتا', 'مكانكم', 'ليستا', 'أيلول', 'أُفٍّ', 'س',
                    'خبَّر', 'عجبا', 'نَّ', 'لم', 'الذين', 'تسعة', 'فإن', 'غالبا', 'ليسا', 'ساء', 'أكثر', 'تعسا',
                    'إياها', 'إذ', 'ذلكما', 'بكما', 'ع', 'به', 'غادر', 'ذاك', 'بكم', 'صبرا', 'نفس', 'مما', 'كاف',
                    'ثلاثاء', 'قلما', 'اللذين', 'تي', 'إليكن', 'طاق', 'هذه', 'آهٍ', 'هَاتانِ', 'ذلك', 'ك', 'عوض', 'سوف',
                    'أفريل', 'أوه', 'غ', 'فلس', 'قد', 'آهاً', 'لهم', 'تِي', 'ه', 'إى', 'ح', 'أقبل', 'أبٌ', 'ذان', 'فيه',
                    'مع', 'هم', 'ثمان', 'لعل', 'ثلاث', 'أيّان', 'سنتيم', 'فلا', 'سبعون', 'آمينَ', 'التي', 'نا', 'هيهات',
                    'أطعم', 'وا', 'خمسمئة', 'أحد', 'مايو', 'كذلك', 'دونك', 'أهلا', 'فإذا', 'طَق', 'خمس', 'ثمانمئة',
                    'يناير', 'تسعمئة', 'لام', 'آها', 'منذ', 'بخ', 'أو', 'شبه', 'كلتا', 'أنا', 'كثيرا', 'ذوا', 'فرادى',
                    'أوّهْ', 'إحدى', 'ثمّ', 'معاذ', 'فيما', 'أولاء', 'هن', 'دون', 'أعلم', 'هكذا', 'بمن', 'منها',
                    'رُبَّ', 'مارس', 'اللائي', 'سمعا', 'منه', 'إلا', 'كأيّ', 'علم', 'أمّا', 'كليهما', 'ت', 'تلكما',
                    'أمس', 'بكن', 'أخو', 'تلكم', 'أمام', 'ألا', 'أبريل', 'ثلاثمائة', 'خمسمائة', 'ذَيْنِ', 'والذين',
                    'نحو', 'سادس', 'شمال', 'أنشأ', 'جميع', 'سابع', 'اثنين', 'هنا', 'هلم', 'حيَّ', 'إنَّ', 'ة', 'عَدَسْ',
                    'سبت', 'ياء', 'أ', 'لكنَّ', 'واحد', 'انقلب', 'أنى', 'ذينك', 'عما', 'غين', 'سرا', 'كيفما', 'أول'}
french_stopwords = {'ses', 's', 'étantes', 'me', 'eûmes', 'eurent', 'n', 'pour', 'un', 'ou', 'aurait', 'mes', 'serions',
                    'j', 'fussiez', 'fusse', 'aux', 'à', 'fut', 'le', 'eût', 'avaient', 'eu', 'notre', 'êtes', 'aurais',
                    'ait', 'étante', 'seras', 'as', 'fûmes', 'étions', 'la', 'suis', 'aviez', 'fûtes', 'aie', 'qu',
                    'fussions', 'l', 'avez', 'votre', 'aurez', 'ils', 'elle', 'ai', 'avons', 'avions', 'des', 'eûtes',
                    'même', 'soyons', 'auront', 'serai', 'leur', 'une', 'moi', 'étais', 'ne', 'était', 'eussiez', 'ce',
                    'ta', 'et', 'tes', 'eut', 'avec', 'c', 'aies', 'au', 'ayants', 'te', 'est', 'toi', 'mais', 'ayante',
                    'aurai', 'sera', 'eusses', 'y', 'ayez', 'étés', 'eus', 'vos', 'de', 'ces', 'eue', 'ont', 'nos',
                    'aurons', 'étée', 'fût', 'eux', 'été', 'd', 'soyez', 'les', 'nous', 'eussent', 't', 'seraient',
                    'on', 'je', 'sa', 'étiez', 'soient', 'ayantes', 'lui', 'sommes', 'par', 'ayons', 'sur', 'sont',
                    'en', 'avais', 'ma', 'du', 'ton', 'm', 'tu', 'seriez', 'serait', 'étants', 'avait', 'aient', 'eues',
                    'mon', 'seront', 'se', 'es', 'ayant', 'eussions', 'dans', 'étant', 'serons', 'fusses', 'auras',
                    'pas', 'fussent', 'soit', 'étaient', 'étées', 'il', 'que', 'eusse', 'son', 'serez', 'furent',
                    'aura', 'aurions', 'qui', 'vous', 'serais', 'fus', 'sois', 'auraient', 'auriez'}
spanish_stopwords = {'habían', 'hayas', 'me', 'nuestros', 'nuestro', 'vuestro', 'estabais', 'sentidas', 'con', 'hubo',
                     'estaríamos', 'suyas', 'desde', 'estada', 'sintiendo', 'tienen', 'habrían', 'nosotras', 'ti',
                     'vuestra', 'hube', 'serán', 'estuvieron', 'estuviste', 'hubiéramos', 'estando', 'estés', 'estas',
                     'todos', 'tuyas', 'seríamos', 'vosotros', 'haya', 'sentidos', 'estamos', 'tuviesen', 'habría',
                     'les', 'ellas', 'fueses', 'estemos', 'a', 'cuando', 'porque', 'ante', 'estuvo', 'tuviera',
                     'nosotros', 'fuese', 'tuvieseis', 'estuvimos', 'fuimos', 'tenía', 'había', 'estuvieseis',
                     'algunas', 'hubieses', 'sobre', 'tened', 'tenían', 'estuviésemos', 'son', 'durante', 'hayáis',
                     'tenida', 'ella', 'mucho', 'hubiesen', 'muchos', 'estarían', 'habíamos', 'tendrías', 'seréis',
                     'hasta', 'será', 'yo', 'tuya', 'algo', 'teníamos', 'mío', 'seamos', 'estos', 'están', 'tenéis',
                     'vosotras', 'hubisteis', 'nuestras', 'para', 'al', 'sí', 'hubiese', 'contra', 'sean', 'estuvieras',
                     'estuvisteis', 'todo', 'estarás', 'por', 'tuyo', 'tendrán', 'tanto', 'nos', 'algunos', 'muy',
                     'hubiera', 'serían', 'fueras', 'nuestra', 'suyos', 'habrá', 'suyo', 'otra', 'tuve', 'tienes',
                     'seríais', 'tendrás', 'tuvieron', 'hayan', 'mi', 'estaría', 'seas', 'habías', 'fuiste', 'fueseis',
                     'sería', 'sus', 'es', 'seremos', 'unos', 'tenemos', 'fuera', 'del', 'una', 'tendrá', 'quienes',
                     'tendríamos', 'como', 'ha', 'tenidas', 'habida', 'habríais', 'tuvimos', 'las', 'suya', 'tengan',
                     'habidos', 'tendríais', 'tengo', 'estaremos', 'esos', 'estarías', 'quien', 'sentido', 'seré', 'un',
                     'serías', 'tuvieras', 'hubierais', 'teníais', 'estéis', 'estábamos', 'he', 'éramos', 'habéis',
                     'tiene', 'habrías', 'tendremos', 'tenido', 'míos', 'donde', 'fui', 'eso', 'eras', 'estarán',
                     'estuviéramos', 'soy', 'estuvierais', 'siente', 'hubimos', 'hubieran', 'y', 'estuviese', 'también',
                     'de', 'han', 'erais', 'antes', 'habidas', 'los', 'el', 'estaréis', 'estaré', 'tendré', 'tuviese',
                     'estad', 'esa', 'habremos', 'fuerais', 'estuvieran', 'habrán', 'en', 'más', 'estado', 'vuestros',
                     'serás', 'otros', 'se', 'estuvieses', 'tendría', 'habré', 'entre', 'sentid', 'tendrían',
                     'teniendo', 'estados', 'mías', 'habrás', 'habríamos', 'que', 'mía', 'estaba', 'hubieseis', 'tuvo',
                     'habíais', 'fueran', 'hayamos', 'fue', 'estar', 'otras', 'tuvieses', 'este', 'estaban', 'has',
                     'estás', 'ya', 'le', 'estabas', 'hemos', 'estará', 'cual', 'os', 'estuviera', 'e', 'la',
                     'hubieras', 'estoy', 'qué', 'tuviste', 'uno', 'estén', 'era', 'estáis', 'tuvierais', 'somos',
                     'eran', 'ellos', 'tengamos', 'su', 'pero', 'tuvisteis', 'nada', 'tuviéramos', 'ese', 'tengas',
                     'tuyos', 'hubiste', 'tenga', 'hubiésemos', 'hay', 'tuviésemos', 'te', 'fuisteis', 'lo', 'poco',
                     'estadas', 'vuestras', 'él', 'habiendo', 'otro', 'estaríais', 'sea', 'eres', 'mí', 'mis', 'tenías',
                     'tengáis', 'fuéramos', 'tus', 'esas', 'esta', 'está', 'tendréis', 'seáis', 'hubieron', 'tu', 'o',
                     'fuesen', 'no', 'tú', 'fueron', 'habido', 'sentida', 'tenidos', 'sin', 'estuviesen', 'tuvieran',
                     'estuve', 'ni', 'esté', 'habréis', 'esto', 'sois', 'fuésemos'}
russian_stopwords = {'не', 'ну', 'в', 'разве', 'куда', 'них', 'чтобы', 'там', 'я', 'после', 'над', 'за', 'всех', 'этот',
                     'может', 'нельзя', 'много', 'свою', 'вас', 'надо', 'тут', 'хоть', 'ему', 'два', 'тогда', 'об',
                     'где', 'такой', 'опять', 'эту', 'ее', 'но', 'на', 'со', 'теперь', 'уж', 'него', 'три', 'ничего',
                     'с', 'раз', 'нас', 'моя', 'вдруг', 'эти', 'была', 'быть', 'про', 'того', 'по', 'под', 'как', 'из',
                     'мы', 'потому', 'между', 'какой', 'она', 'совсем', 'ж', 'и', 'всегда', 'им', 'был', 'были', 'да',
                     'когда', 'наконец', 'во', 'бы', 'о', 'больше', 'все', 'а', 'при', 'себя', 'от', 'его', 'тем',
                     'том', 'ним', 'к', 'ведь', 'нет', 'здесь', 'иногда', 'так', 'почти', 'сейчас', 'то', 'этого', 'вы',
                     'всего', 'сам', 'перед', 'другой', 'чтоб', 'кто', 'более', 'себе', 'уже', 'конечно', 'меня', 'он',
                     'ей', 'или', 'их', 'даже', 'чем', 'нибудь', 'они', 'потом', 'же', 'вот', 'чего', 'мой', 'зачем',
                     'впрочем', 'вам', 'ней', 'мне', 'этом', 'один', 'тоже', 'хорошо', 'что', 'ты', 'тебя', 'если',
                     'нее', 'тот', 'через', 'всю', 'еще', 'лучше', 'у', 'без', 'никогда', 'этой', 'только', 'есть',
                     'будет', 'будто', 'можно', 'ни', 'чуть', 'ли', 'для', 'какая', 'было', 'до'}


def multiple_stopwords(*args):
    result = set()
    import sys
    current_module = sys.modules[__name__]

    for lang in args:
        if lang not in ['english', 'chinese', 'arabic', 'french', 'spanish', 'russian']:
            logger.warning(f'unsupported language: {lang}')

        result = result.union(getattr(current_module, f'{lang}_stopwords'))

    return result